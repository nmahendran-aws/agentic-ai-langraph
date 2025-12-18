from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage

class Movie(TypedDict):
    name: str
    genre: str
    year: int

movie = Movie(name="Inception", genre="Sci-Fi", year=2010)
print(movie)