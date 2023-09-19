from pydantic import BaseModel, Field
from typing import Optional

#То что требуется при первом создании
class BookBase(BaseModel):
    name:str = Field(title='Название книги')
    date: str = Field(title='Дата прочтения')  # Предполагается, что дата представлена строкой
    rating: int = Field(title='Оценка книги', ge=0, le=10)  # Ограничение оценки от 0 до 10
    genres: list[str] = Field(title='Жанры книги')  # Жанры в виде списка строк
    type: str = Field(title='Тип книги')  # Предполагаем, что тип книги может быть "художественная", "научная" и т.д.
    authors: list[str] = Field(title='Авторы книги') # Предполагаем, что авторы книги представлены списком строк
    series: Optional[str] = Field(title='Принадлежность к серии')
    about: Optional[str] = Field(title='Описание книги')
    
class Book(BookBase):
    id: int = Field(title='Идентификатор книги')