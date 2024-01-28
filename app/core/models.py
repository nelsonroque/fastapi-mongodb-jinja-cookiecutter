from pydantic import BaseModel, Field
from typing import List, Optional
from core.utils import get_utc_timestamp, gen_uid#, get_current_month, get_current_day, get_current_year
from datetime import datetime, timezone

# class DocumentIds(BaseModel):
#     id: Optional[str] = Field(default_factory=gen_uid)

# borrow private key approach

# Specify the schema for the Post model
class Post(BaseModel):#, TimestampIds):
    #uid: str = Field(default_factory=lambda: gen_uid())
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

class Status(BaseModel):
    status: str
    error: Optional[str] = None
    deleted_count: Optional[int] = None
    matched_count: Optional[int] = None
    modified_count: Optional[int] = None

class Log(BaseModel):
    created_utc: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

#     timestamp: datetime
#     host: str
#     method: str
#     url: str
#     headers: dict