import pytest
from service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self, genre_service):
        genre = self.genre_service.get_one(1)

        assert genre is not None
        assert genre.id is not None


    def test_get_all(self):
        genres = self.genre_service.get_all()

        assert len(genres) > 0
        assert isinstance(genres, list)

    def test_create(self):
        genre_test = {
            "name": "Vadim"
        }
        genre = self.genre_service.create(genre_test)

        assert genre.id is not None

    def test_delete(self):
        delete_genre = self.genre_service.dao.delete(3)

        assert delete_genre == {'answer': 'success'}

    def test_update(self):
        update_data = {
            "id": 5,
            "name": "Vadim"
        }
        genre = self.genre_service.dao.update(update_data)

        assert genre == {"updated_rows": 1, "id": "5", "answer": "updated"}

