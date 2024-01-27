from fastapi import FastAPI, APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# =============================================================================

router = APIRouter(
    prefix="/ui",
    tags=["ui"]
)
templates = Jinja2Templates(directory="templates")

# =============================================================================

@router.get("/test")
async def render_frontend():
    return HTMLResponse("<h1>Hello</h1>", status_code=200)


@router.get("/homepage")
async def render_frontend(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

#     token: str = Depends(oauth2_scheme),
#     commons: dict = Depends(common_parameters),
# ):
#     user = decode_token(token)