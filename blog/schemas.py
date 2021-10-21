from pydantic import BaseModel
from typing import List, Optional

class Blog(BaseModel):
    title: str
    body: str
    #riblah: str
    #published_at: Optional[bool]
    class Config:
        orm_mode = True
    pass

class User(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True
    pass

class ShowUser(BaseModel):
    name: str
    email: str
    blog: List[Blog] = []
    class Config:
        orm_mode = True
    pass

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config:
        orm_mode = True
    pass

class DeleteBlog(BaseModel):
    message: str
    class Config:
        orm_more = True
    pass

class Login(BaseModel):
    username: str
    password: str
    class Config:
        orm_mode = True
    pass

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None