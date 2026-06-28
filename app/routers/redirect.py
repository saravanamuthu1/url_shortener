from fastapi import APIRouter,Depends,HTTPException,status

router = APIRouter()

@router.get("/{short_code}",status_code=status.HTTP_302_FOUND)
async def redirect_url():
    pass

