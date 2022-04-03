from datetime import datetime

import ormar

from core.db import BaseModel, BaseMeta


class Url(BaseModel):
    class Meta(BaseMeta):
        abstract = False

    original_url: str = ormar.String(max_length=200)
    short_path: str = ormar.String(max_length=50, unique=True)
    time_start: datetime = ormar.DateTime(auto_now_add=True)
    time_end: datetime = ormar.DateTime()
