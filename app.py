"""Sinema Bilet Rezervasyon Sistemi — başlangıç Flask uygulaması."""

from flask import Flask, render_template


def create_app():
    """Flask uygulamasını oluştur ve sayfa yollarını tanımla."""
    app = Flask(__name__)

    @app.get("/")
    def home():
        """Ana sayfayı göster."""
        return render_template("index.html")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
