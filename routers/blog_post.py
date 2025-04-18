from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"]
)


class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]

#body, path param, query param -- sequence of function parameters
@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int , version: int = 1):
    return { 
        'id' : id,
        'data' : blog,
        'version': version
        }