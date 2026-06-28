from fastapi import FastAPI
from router import auth,url,redirect

app = FastAPI()

app.include_router(auth.router)
app.include_router(url.router)
app.include_router(redirect.router)