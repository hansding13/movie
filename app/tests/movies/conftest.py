# app/tests/movies/conftest.py

import pytest

from movies.models import Movie


@pytest.fixture(scope="function")
def add_movie():
    def _add_movie(title, genre, year, language, adult_rating):
        movie = Movie.objects.create(
            title=title,
            genre=genre,
            year=year,
            language=language,
            adult_rating=adult_rating,
        )
        return movie

    return _add_movie
