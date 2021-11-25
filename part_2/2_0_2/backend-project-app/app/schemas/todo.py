from pydantic import BaseModel,Field, validator


class Todo(BaseModel):
    todo: str = Field(..., description="Todo content", example="make an appointment")

    @validator('todo')
    def todo_no_empty_not_greater_than_140_char(cls, v):
        if not v or not (v.strip()):
            raise ValueError('Empty strings are not allowed.')
        elif len(v) > 140:
            raise ValueError('Todo message cannot exceed 140 characters')
        return v
