import pytest
from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self, movie_service):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None


    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0
        assert isinstance(movies, list)

    def test_create(self):
        movie_test = {
            'title': "title_5",
            'description': "description_5",
            'trailer': "trailer_5",
            'year': 2001,
            'rating': 9.8,
            'genre_id': 1,
            'director_id': 3
        }
        movie = self.movie_service.create(movie_test)

        assert movie.id is not None

    def test_delete(self):
        delete_movie = self.movie_service.dao.delete(3)

        assert delete_movie == {'answer': 'success'}

    def test_update(self):
        update_data = {
            'id': 2,
            'title': "title_4",
            'description': "description_4",
            'trailer': "trailer_4",
            'year': 2007,
            'rating': 8.8,
            'genre_id': 2,
            'director_id': 1
        }
        movie = self.movie_service.dao.update(update_data)

        assert movie == {"updated_rows": 1, "id": "2", "answer": "updated"}

