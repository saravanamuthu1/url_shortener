from fastapi import APIRouter,Depends,HTTPException,status

router = APIRouter(prefix="/auth",tags=["Auth"])

@router.post("/signup",status_code=status.HTTP_201_CREATED)
async def sign_up():
    pass


@router.post("/login",status_code=status.HTTP_200_OK)
async def login():
    pass

@router.post("/token",status_code=status.HTTP_201_CREATED)
async def generate_token():
    pass