"""Ana sayfa için başlangıç testleri (pytest)."""

from app import create_app


def test_home_returns_success():
    """Ana sayfa HTTP 200 döndürmelidir."""
    client = create_app().test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_project_name():
    """Ana sayfa proje adını göstermelidir."""
    client = create_app().test_client()
    response = client.get("/")
    assert b"Sinema Bilet Rezervasyon Sistemi" in response.data
