from fastapi import FastAPI, APIRouter
from fastapi.responses import HTMLResponse

# =============================================================================

router = APIRouter(
    prefix="/ui",
    tags=["ui"]
)

# =============================================================================

@router.get("/test")
async def render_frontend():
    return HTMLResponse("<h1>Hello</h1>", status_code=200)


#     token: str = Depends(oauth2_scheme),
#     commons: dict = Depends(common_parameters),
# ):
#     user = decode_token(token)