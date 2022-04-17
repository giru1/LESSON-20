import pytest
from unittest.mock import MagicMock
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService


@pytest.fixture()
def movie_service():
    dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title='Йеллоустоун',
        description='Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        trailer='www.youtube.com/',
        year=2018,
        rating=8.6,
        genre_id=17,
        director_id=1
    )

    dao.get_one = MagicMock(return_value=
    {
        'id': 1,
        'title': 'Йеллоустоун',
        'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        'trailer': 'www.youtube.com/',
        'year': 2018,
        'rating': 8.6,
        'genre_id': 17,
        'director_id': 1
    })

    dao.get_one = MagicMock(return_value=
        [
            {
                'id': 1,
                'title': 'Йеллоустоун',
                'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
                'trailer': 'www.youtube.com/',
                'year': 2018,
                'rating': 8.6,
                'genre_id': 17,
                'director_id': 1
            },
            {
                'id': 1,
                'title': 'Йеллоустоун',
                'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
                'trailer': 'www.youtube.com/',
                'year': 2018,
                'rating': 8.6,
                'genre_id': 17,
                'director_id': 1
            }
        ]
    )

    dao.create = MagicMock(return_value={
        'id': 1,
        'title': 'Йеллоустоун 2',
        'description': 'Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        'trailer': 'www.youtube.com/',
        'year': 2018,
        'rating': 8.6,
        'genre_id': 17,
        'director_id': 1
    })
    dao.update = MagicMock(return_value={
        'id': 1,
        'title': 'Йеллоустоун 3',
        'description': '1Владелец ранчо пытается сохранить землю своих предков. Кевин Костнер в неовестерне от автора «Ветреной реки»',
        'trailer': 'www.youtube.com/1',
        'year': 2022,
        'rating': 10,
        'genre_id': 17,
        'director_id': 1
    })
    dao.delete = MagicMock(return_value={})


class TestMovieService:
    def test_get_one(self):
        pass

    def test_get_all(self):
        pass

    def test_delete(self):
        pass

    def test_update(self):
        pass

    def test_create(self):
        pass
