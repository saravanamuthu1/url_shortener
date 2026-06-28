from fastapi import APIRouter,Depends,HTTPException,status

router = APIRouter(prefix="/urls",tags=["urls"])

@router.post("/shorten",status_code=status.HTTP_201_CREATED)
async def create_short_url():
    pass

@router.get("/all",status_code=status.HTTP_200_OK)
async def get_all_urls():
    pass


@router.get("/{short_code}/analytics",status_code=status.HTTP_200_OK)
async def get_analytics():
    pass

@router.get("/{short_code}",status_code=status.HTTP_200_OK)
async def get_url_details():
    pass

@router.patch("/{short_code}")
async def update_url():
    pass

@router.delete("/{short_code}")
async def delete_url():
    pass

@router.post("/{short_code}/permissions")
async def add_permission():
    pass

@router.delete("/{short_code}/permissions/{user_id}")
async def remove_permission():
    pass
