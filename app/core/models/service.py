from datetime import datetime

from pydantic import BaseModel, Field
from typing import List


class ApiAnswerInfo(BaseModel):
    """
    Answer fields schema
    """
    string_field: str = Field(
        title="title",
        description="description",
        example="example"
        )
    integer_field: int = Field(
        title="title",
        description="description",
        example="1"
        )
    float_field: float = Field(
        title="title",
        description="description",
        example="1.5"
        )
    datetime_field: datetime = Field(
        title="title",
        description="description",
        example="2020-01-01T00:00:00"
        )

class ApiAnswer(BaseModel):
    """
    Answer schema
    """
    answer: ApiAnswerInfo

class ApiResponse(BaseModel):
    """
    Service response schema 
    """
    info: List[ApiAnswer] = Field(
        title="info",
        description="description"
        )


