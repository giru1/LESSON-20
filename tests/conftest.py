from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO


@pytest.fixture
def director_dao():
    dao = DirectorDAO(None)

    director_1 = Director(id=1, name="Ben")
    director_2 = Director(id=2, name="Stevin")
    director_3 = Director(id=3, name="John")

    dao.get_one = MagicMock(return_value=director_1)
    dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    dao.update = MagicMock(return_value={"updated_rows": 1, "id": "2", "answer": "updated"})
    dao.create = MagicMock(return_value=director_2)
    dao.delete = MagicMock(return_value={'answer': 'success'})

    return dao


@pytest.fixture
def genre_dao():
    dao = GenreDAO(None)

    genre_1 = Genre(id=1, name="Comedy")
    genre_2 = Genre(id=2, name="Action")
    genre_3 = Genre(id=3, name="Trailer")

    dao.get_one = MagicMock(return_value=genre_1)
    dao.get_all = MagicMock(return_value=[genre_1, genre_2, genre_3])
    dao.update = MagicMock(return_value={"updated_rows": 1, "id": "5", "answer": "updated"})
    dao.create = MagicMock(return_value=genre_2)
    dao.delete = MagicMock(return_value={'answer': 'success'})

    return dao


@pytest.fixture
def movie_dao():
    dao = MovieDAO(None)

    movie_1 = Movie(id=1, title="title_1", description="description_1", trailer="trailer_1",
                    year=2001, rating=9.8, genre_id=2, director_id=1)
    movie_2 = Movie(id=2, title="title_2", description="description_2", trailer="trailer_2",
                    year=1990, rating=7.0, genre_id=1, director_id=3)
    movie_3 = Movie(id=3, title="title_3", description="description_3", trailer="trailer_3",
                    year=1994, rating=9.0, genre_id=3, director_id=2)

    dao.get_one = MagicMock(return_value=movie_1)
    dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    dao.update = MagicMock(return_value={"updated_rows": 1, "id": "2", "answer": "updated"})
    dao.create = MagicMock(return_value=movie_2)
    dao.delete = MagicMock(return_value={'answer': 'success'})

    return dao
