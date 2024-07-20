from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class OpenAIMessageRole(Enum):
    SYSTEM = 'system'
    USER = 'user'
    ASSISTANT = 'assistant'


class Conversation(BaseModel):
    role: str
    content: str


class Session(BaseModel):
    conversations: List[Conversation] = []
    generated_response: Optional[dict] = None
    status: str = "pending"
