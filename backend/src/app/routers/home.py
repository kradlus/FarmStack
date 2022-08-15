from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from app.utils import get_current_active_user
from app.models import User

router: APIRouter = APIRouter()


@router.get("/")
async def home_root(
    current_user: User = Depends(get_current_active_user),
) -> JSONResponse:
    return JSONResponse(
        content={"user": current_user.username}, status_code=status.HTTP_200_OK
    )
