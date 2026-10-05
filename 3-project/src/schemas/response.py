from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    # attributes
    status_code: int = 200
    message: str
    data: Optional[T] = None
