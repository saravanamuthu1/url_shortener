from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Url
from sqlalchemy import select
from app.redis import get_redis 
from datetime import datetime, UTC
from redis.asyncio import Redis
import json
from fastapi.responses import RedirectResponse
from fastapi import BackgroundTasks
from app.database import async_session
from app.models import RedirectEvent
from fastapi import Request

router = APIRouter()

async def record_redirect(short_code: str, ip: str):
    
    event = RedirectEvent(
        short_code=short_code,
        ip_address=ip,
    )
    async with async_session() as session:
        session.add(event)
        await session.commit()      
    

@router.get("/{short_code}",status_code=status.HTTP_302_FOUND)
async def redirect_url(
    short_code:str,
    request:Request, 
    background_tasks: BackgroundTasks, 
    db: AsyncSession = Depends(get_db), 
    redis:Redis = Depends(get_redis)):

    ip = request.client.host
    cached_url = await redis.get(f"url:{short_code}")
    if cached_url:
        url_data = json.loads(cached_url)
        if url_data["expires_at"] and datetime.fromisoformat(url_data["expires_at"]) < datetime.now(UTC):
            raise HTTPException(status_code=status.HTTP_410_GONE, detail="URL has expired")
        if not url_data["is_public"]:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="URL is private")
        background_tasks.add_task(record_redirect,short_code,ip)
        return RedirectResponse(url=url_data["original_url"], status_code=status.HTTP_302_FOUND)
    else:
        stmt = select(Url).where(Url.short_alias == short_code)
        result = await db.execute(stmt)
        url_obj = result.scalar_one_or_none()
        if not url_obj:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")           
        if url_obj.expires_at and url_obj.expires_at < datetime.now(UTC):
            raise HTTPException(status_code=status.HTTP_410_GONE, detail="URL has expired")
        if not url_obj.is_public:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="URL is private")
        await  redis.set(f"url:{short_code}",json.dumps({"original_url":url_obj.original_url,"expires_at":url_obj.expires_at.isoformat() if url_obj.expires_at else None,"is_public":url_obj.is_public}),ex=3600)
        background_tasks.add_task(record_redirect,short_code,ip)
        return RedirectResponse(url=url_obj.original_url, status_code=status.HTTP_302_FOUND)

