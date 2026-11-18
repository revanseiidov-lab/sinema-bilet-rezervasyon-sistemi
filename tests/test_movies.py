"""Hafta 02 film kataloğu ve SQLite bütünlük testleri."""

import sqlite3

import pytest

from app import create_app
from db import DEMO_MOVIES, get_db, init_db, list_movies


@pytest.fixture
def app(tmp_path):
    return create_app({"TESTING": True, "DATABASE": tmp_path / "test.sqlite3"})


def test_init_command_creates_movies_table(app):
    result = app.test_cli_runner().invoke(args=["init-db"])
    assert result.exit_code == 0, result.output
    assert app.config["DATABASE"].is_file()
    with app.app_context():
        columns = get_db().execute("PRAGMA table_info(movies)").fetchall()
    assert [column["name"] for column in columns] == [
        "id", "title", "genre", "duration_minutes", "description", "release_year",
    ]


def test_demo_data_matches_expected_catalog(app):
    with app.app_context():
        init_db()
        movies = list_movies()
    assert 5 <= len(movies) <= 8
    assert {tuple(movie) for movie in movies} == set(DEMO_MOVIES)


def test_reinitialization_preserves_existing_movies(app):
    with app.app_context():
        init_db()
        connection = get_db()
        with connection:
            connection.execute(
                "UPDATE movies SET description = ? WHERE title = ?",
                ("Güncellenmiş açıklama", DEMO_MOVIES[0][0]),
            )
        init_db()
        movies = list_movies()
    assert len(movies) == len(DEMO_MOVIES)
    assert any(movie["description"] == "Güncellenmiş açıklama" for movie in movies)


def test_movies_page_reads_database(app):
    with app.app_context():
        init_db()
        connection = get_db()
        with connection:
            connection.execute(
                """
                INSERT INTO movies (title, genre, duration_minutes, description, release_year)
                VALUES (?, ?, ?, ?, ?)
                """,
                ("Deneme Filmi", "Macera", 123, "Yalnızca test veritabanında var.", 2020),
            )
    client = app.test_client()
    assert b'href="/filmler"' in client.get("/").data
    response = client.get("/filmler")
    assert response.status_code == 200
    page = response.get_data(as_text=True)
    for value in ("Deneme Filmi", "Macera", "123 dk", "Yalnızca test veritabanında var.", "2020"):
        assert value in page


def test_empty_catalog(app):
    with app.app_context():
        init_db()
        connection = get_db()
        with connection:
            connection.execute("DELETE FROM movies")
    response = app.test_client().get("/filmler")
    assert response.status_code == 200
    assert "Henüz listelenecek film yok." in response.get_data(as_text=True)


def test_unavailable_catalog_hides_sqlite_details(app):
    response = app.test_client().get("/filmler")
    assert response.status_code == 503
    page = response.get_data(as_text=True)
    assert "Film listesi şu anda görüntülenemiyor." in page
    assert "no such table" not in page
    assert "test.sqlite3" not in page


@pytest.mark.parametrize(
    ("column", "invalid_value"),
    [
        ("title", None), ("title", "  "), ("genre", ""),
        ("duration_minutes", 0), ("duration_minutes", 2.5),
        ("description", "\t"), ("release_year", 1800), ("release_year", 2020.5),
    ],
)
def test_invalid_movie_is_rejected(app, column, invalid_value):
    movie = dict(zip(
        ("title", "genre", "duration_minutes", "description", "release_year"),
        ("Deneme Filmi", "Macera", 123, "Geçici kayıt.", 2020),
    ))
    movie[column] = invalid_value
    with app.app_context():
        init_db()
        connection = get_db()
        with pytest.raises(sqlite3.IntegrityError), connection:
            connection.execute(
                """
                INSERT INTO movies (title, genre, duration_minutes, description, release_year)
                VALUES (:title, :genre, :duration_minutes, :description, :release_year)
                """,
                movie,
            )
