from fastapi import APIRouter, Response, Body, Depends, Request
from fastapi.templating import Jinja2Templates

# =============================================================================

# --- create router ---
router = APIRouter()
templates = Jinja2Templates(directory="templates")

# =============================================================================


# load dashboard for admins ---
@router.get("/blog")
async def get_all_blogs(request: Request):
    # TODO read from DB
    posts = [
        {
            "title": "Blog 1",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        },
        {
            "title": "Blog 2",
            "content": "Fusce euismod lectus in enim feugiat, a posuere sapien sollicitudin.",
        },
        {
            "title": "Blog 3",
            "content": "Vestibulum hendrerit enim eget neque lacinia, non tincidunt purus dignissim.",
        },
        {
            "title": "Blog 4",
            "content": "Pellentesque vel nunc at neque ultrices rhoncus.",
        },
        {
            "title": "Blog 5",
            "content": "Aliquam id justo at leo eleifend viverra nec nec ex.",
        },
        {
            "title": "Blog 6",
            "content": "Aenean in arcu ut elit vehicula volutpat nec nec odio.",
        },
        {"title": "Blog 7", "content": "Sed eget velit a erat pellentesque interdum."},
        {
            "title": "Blog 8",
            "content": "Phasellus cursus tortor a consectetur sodales.",
        },
        {
            "title": "Blog 9",
            "content": "Cras euismod nunc vel urna ullamcorper, a scelerisque libero congue.",
        },
        {"title": "Blog 10", "content": "Quisque consequat urna at aliquam tincidunt."},
    ]
    return templates.TemplateResponse("blog.html", {"posts": posts, "request": request})


# =============================================================================
