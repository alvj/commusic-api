from datetime import datetime
from sqlmodel import SQLModel


class Token(SQLModel):
    access_token: str
    token_type: str
    expires: datetime
