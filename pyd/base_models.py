from pydantic import BaseModel, Field


class BaseBook(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="Огни Алапаевска")
    author: str = Field(example="Иванов И.И.")
    year: int = Field(example=2023)
    genre: str = Field(example="Фантастика")
