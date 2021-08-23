from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title: str
    body: str
    #blah: str
    published_at: Optional[bool]