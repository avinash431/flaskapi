import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.get("/blog")
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    # Only get 10 published docs
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "unpublished"}


@app.get("/blog/{blog_id}")
def show(blog_id: int):
    return {"data": blog_id}


@app.get("/blog/{blog_id}/comments")
def comments(blog_id):
    return {"data": f"comments for {blog_id}"}


@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"blog created with the title {request.title} and body is {request.body}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
