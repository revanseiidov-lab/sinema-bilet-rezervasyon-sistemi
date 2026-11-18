"""Sinema Bilet Rezervasyon Sistemi — başlangıç Flask uygulaması."""

import sqlite3
from pathlib import Path

from flask import Flask, render_template


from db import close_db, init_db_command, list_movies


def create_app(config=None):
    """Flask uygulamasını oluştur ve sayfa yollarını tanımla."""
    app = Flask(__name__)

    app.config.from_mapping(DATABASE=Path(app.instance_path) / "cinema.sqlite3")
    if config is not None:
        app.config.update(config)
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

    @app.get("/")
    def home():
        """Ana sayfayı göster."""
        return render_template("index.html")

    @app.get("/filmler")
    def movies():
        """SQLite film kataloğunu göster."""
        try:
            films = list_movies()
        except sqlite3.Error:
            app.logger.exception("Film kataloğu okunamadı.")
            return render_template("movies.html", unavailable=True), 503
        return render_template("movies.html", films=films)

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
