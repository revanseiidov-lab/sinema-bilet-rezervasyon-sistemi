# Hafta 02 Test Sonuçları

**Tarih** 18.11.2026  
**Ortam** macOS, Python 3.9.6, pytest 8.4.2, pluggy 1.6.0  
**Komut** `PYTHONDONTWRITEBYTECODE=1 ../.venv/bin/python -m pytest -p no:cacheprovider -v`  
**Sonuç** 16 PASS, 0 FAIL. Kod kapsamı ölçülmedi. Test veritabanları geçicidir.

| Kimlik | Beklenen sonuç | Gözlenen sonuç | Durum |
| --- | --- | --- | --- |
| TC-W01-001 | Ana sayfa HTTP 200 döner | HTTP 200 | PASS |
| TC-W01-002 | Proje adı görünür | Proje adı bulundu | PASS |
| TC-W02-001 | CLI SQLite dosyasını ve altı sütunlu tabloyu oluşturur | Dosya ve sütunlar doğrulandı | PASS |
| TC-W02-002 | 5–8 geçerli örnek film | Beklenen altı kayıt birebir eşleşti | PASS |
| TC-W02-003 | Tekrar başlatma kayıtları çoğaltmaz veya değiştirmez | Sayı ve güncellenmiş açıklama korundu | PASS |
| TC-W02-004 | Bağlantı, HTTP 200 ve SQLite kaydının tüm alanları | Bağlantı ve ayrı test kaydı bulundu | PASS |
| TC-W02-005 | Boş liste HTTP 200 ve açıklama | Türkçe boş liste mesajı görüldü | PASS |
| TC-W02-006 | Okuma hatasında HTTP 503 ve genel mesaj | Türkçe mesaj görüntülendi, SQL ayrıntıları gizlendi | PASS |
| TC-W02-007a–h | Sekiz geçersiz giriş SQLite tarafından reddedilir | Her giriş için IntegrityError | 8 PASS |

FR-01, FR-06 ve NFR-01–03 için Hafta 02 kapsamındaki kontroller yürütüldü. Seans, koltuk ve rezervasyon testleri gelecek haftalara aittir. Sonuçlar macOS ortamında alınmıştır.

[Katalog ekran görüntüsü](../evidence/week-02/film-listesi.jpg) · [HTTP doğrulaması](../evidence/week-02/http-check.txt) · [Pytest çıktısı](../evidence/week-02/pytest-results.txt) · [Hafta 01 raporu](Test_Results_Week_01.md) · [Hata kaydı](Defect_Log.md)
