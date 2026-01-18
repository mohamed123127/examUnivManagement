from pydantic import BaseModel
from typing import Optional

class NotificationCreate(BaseModel):
    message: str
    type: Optional[str] = None
