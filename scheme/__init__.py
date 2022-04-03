from pydantic import BaseModel


class FailedResponse(BaseModel):
    status: bool = False
    error: str
