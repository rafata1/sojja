from typing import Optional

from pydantic import BaseModel


class SendMessageRequest(BaseModel):
    topic: str
    num_words: int
    num_images: int
    keywords: list[str]
    description: Optional[str] = None


class TextToImageRequest(BaseModel):
    prompt: str


class GenerateParagraphRequest(BaseModel):
    prompt: str
    keywords: list[str]
    num_words: int
    previous_paragraph: Optional[str] = None


class GenBlogRequest(BaseModel):
    prompt: str
