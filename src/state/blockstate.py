from typing import TypedDict
from pydantic import BaseModel,Field


class Blog(BaseModel):
        title:str = Field(description= "title of the blog post")
        content:str = Field(description= "content of the blog post")

class BlogState(TypedDict):
        topic:str
        blog:Blog
        language:str

