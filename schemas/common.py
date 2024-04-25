from typing import Any, Optional
from pydantic import BaseModel


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]
    
    class Config:
        json_schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation Successful",
                "data": "sample data",
            }
        }