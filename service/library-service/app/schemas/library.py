from pydantic import BaseModel, Field
from typing import Optional

#То что требуется при первом создании
class BookBase(BaseModel):
    '''
    База книги. Стоит ли разделить на несколько таблиц ?
    '''
    id: int = Field(title='Идентификатор книги', default=None)
    name:str = Field(title='Название книги')
    rating: int = Field(title='Оценка книги', ge=0, le=10)  # Ограничение оценки от 0 до 10
    genres: list[str] = Field(title='Жанры книги')  # Жанры в виде списка строк
    type: str = Field(title='Тип книги')  # Предполагаем, что тип книги может быть "художественная", "научная" и т.д.
    authors: list[str] = Field(title='Авторы книги') # Предполагаем, что авторы книги представлены списком строк
    series: Optional[str] = Field(title='Принадлежность к серии', default=None)
    about: Optional[str] = Field(title='Описание книги', default=None )
    
class Book(BookBase):
    '''
    Используемая при запросе информации о книге
    '''
    id: int = Field(title='Идентификатор книги', default=None)

class BookUpdate(BookBase):
    '''
    Модель для обновления книги
    '''
    pass