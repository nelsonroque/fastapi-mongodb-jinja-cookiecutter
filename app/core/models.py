from pydantic import BaseModel, Field
from typing import List, Optional
from core.utils import get_utc_timestamp#, get_current_month, get_current_day, get_current_year
from datetime import datetime, timezone

# class DocumentIds(BaseModel):
#     id: Optional[str] = Field(default_factory=gen_uid)

#class TimestampIds(BaseModel):
    #created_utc: datetime = Field(default_factory=get_utc_timestamp)
    # created_month_utc: int = get_current_month()
    # created_day_utc: int = get_current_day()
    # created_year_utc: int = get_current_year()
    # borrow private key approach

# Specify the schema for the Post model
class Post(BaseModel):#, TimestampIds):
    created_utc: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    title: str
    description: str
    body: str
    author_id: str
    slug: str
    tags: List[str]
    published: bool

class Posts(BaseModel):
    posts: List[Post]

# class Log(BaseModel):
#     timestamp: datetime
#     host: str
#     method: str
#     url: str
#     headers: dict