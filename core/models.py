from pydantic import BaseModel, Field
from typing import List, Optional
from lib.utils import gen_uid, gen_uuid_str, get_ts_utc, get_current_month, get_current_day, get_current_year
import datetime

class DocumentIds(BaseModel):
    id: Optional[str] = Field(default_factory=gen_uid)

class TimestampIds(BaseModel):
    created_utc: datetime = Field(default_factory=get_ts_utc)
    created_month: int = get_current_month()
    created_day: int = get_current_day()
    created_year: int = get_current_year()
    # borrow private key approach

# Specify the schema for the Post model
class Post(DocumentIds, TimestampIds):
    title: str
    description: str
    body: str
    author_id: str
    slug: str
    tags: List[str]
    published: bool