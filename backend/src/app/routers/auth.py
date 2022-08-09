from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

router:APIRouter = APIRouter(prefix="/auth")

@router.get("/")
async def auth_login():
    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "message":"Provide username and password"
    })

