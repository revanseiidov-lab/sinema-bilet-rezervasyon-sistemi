"""Film kataloğunun SQLite bağlantısı ve başlangıç verileri."""

import sqlite3
from pathlib import Path

import click
from flask import current_app, g
from flask.cli import with_appcontext


DEMO_MOVIES = (
    ("Kıyıdaki Fener", "Drama", 96, "Bir balıkçı, yıllar sonra kasabasına döner.", 2021),
    ("Son Tren", "Gerilim", 105, "Gece yolcuları kapanan bir istasyonda kalır.", 2022),
    ("Kâğıttan Kanatlar", "Animasyon", 82, "İki kardeş uçabilen bir oyuncak yapar.", 2023),
    ("Mavi Yörünge", "Bilim Kurgu", 112, "Bir ekip uzak bir uydudan sinyal alır.", 2024),
    ("Pazar Sabahı", "Komedi", 91, "Mahalle pazarı bir yemek yarışmasına dönüşür.", 2025),
    ("Sessiz Bahçe", "Gizem", 101, "Bir bahçıvan eski bir defteri araştırır.", 2026),
)


def get_db():
    """İstek veya komut boyunca tek bir bağlantı kullan."""
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(_error=None):
    """Uygulama bağlamı kapandığında bağlantıyı bırak."""
    connection = g.pop("db", None)
    if connection is not None:
        connection.close()


def init_db():
    """Tabloyu oluştur ve örnek filmleri yalnızca bir kez ekle."""
    Path(current_app.config["DATABASE"]).parent.mkdir(parents=True, exist_ok=True)
    connection = get_db()
    schema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
    with connection:
        connection.execute(schema)
        connection.executemany(
            """
            INSERT INTO movies (title, genre, duration_minutes, description, release_year)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, release_year) DO NOTHING
            """,
            DEMO_MOVIES,
        )


def list_movies():
    """Katalog alanlarını belirli bir sırayla getir."""
    return get_db().execute(
        """
        SELECT title, genre, duration_minutes, description, release_year
        FROM movies
        ORDER BY title, release_year
        """
    ).fetchall()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Film tablosunu ve örnek verileri hazırla."""
    init_db()
    click.echo("Film veritabanı hazır.")
