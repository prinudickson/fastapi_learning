from fastapi import FastAPI
import schemas

import uvicorn

app = FastAPI()

@app.post('/blog')
def create(request:schemas.Blog):
    return request


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)