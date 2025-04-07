from pydantic import BaseModel, Field


class CreateBook(BaseModel):
    name: str = Field(min_length=3, max_length=255, example="Огни Алапаевска")
    author: str = Field(min_length=3, max_length=255, example="Иванов И.И.")
    year: int = Field(gt=1000, lt=2026, example=2023)
    genre: str = Field(min_length=3, max_length=255, example="Фантастика")
