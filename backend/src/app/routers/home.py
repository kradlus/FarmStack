from fastapi import APIRouter
from fastapi.responses import JSONResponse

router:APIRouter = APIRouter()

@router.get("/")
async def home_root() -> JSONResponse:
    return JSONResponse(status_code=200, content={
        "detail":"Working"
    })


