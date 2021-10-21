from fastapi import FastAPI
import models
from database import engine
import routers.blog as blog
import routers.user as user
import routers.authentication as authentication

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
