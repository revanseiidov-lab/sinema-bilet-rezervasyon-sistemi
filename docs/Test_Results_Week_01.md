# Hafta 01 — Test Çalıştırma Sonuçları (STR başlangıç kaydı)

**Tarih:** 05.11.2026 (yerel ekran görüntüsündeki tarih)  
**Çalıştıran:** Revan Seiidov  
**Ortam:** macOS (darwin), Python 3.9.6, pytest 8.4.2, pluggy 1.6.0  
**Komut:** `python3 -m pytest -v`  
**Kapsam:** Flask uygulamasının ana sayfası; henüz rezervasyon işlevleri geliştirilmedi.

| Test kimliği | Açıklama | Sonuç |
| --- | --- | --- |
| TC-W01-001 | `test_home_returns_success` — ana sayfa HTTP 200 | PASS |
| TC-W01-002 | `test_home_contains_project_name` — proje adı görüntüleniyor | PASS |

**Özet:** 2 test toplandı; 2 PASS; 0 FAIL; toplam süre 0.09 saniye.

**Manuel doğrulama:** Flask geliştirme sunucusu `http://127.0.0.1:5000` üzerinde açıldı; ana sayfa Safari'de görüntülendi. Terminalde `GET /` için HTTP 200 gözlendi.

**Kanıt durumu:** Üç ekran görüntüsü GitHub deposuna yüklenmiştir (commit: [41fb212](https://github.com/revanseiidov-lab/sinema-bilet-rezervasyon-sistemi/commit/41fb2127c8af3cc987c735c29028b6693103acd3)).

- [Kanban panosu](https://github.com/revanseiidov-lab/sinema-bilet-rezervasyon-sistemi/blob/main/evidence/week-01/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%E2%80%94%202026-11-05%20%D0%B2%2001.49.27.png)
- [Flask ana sayfası](https://github.com/revanseiidov-lab/sinema-bilet-rezervasyon-sistemi/blob/main/evidence/week-01/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%E2%80%94%202026-11-05%20%D0%B2%2001.54.19.png)
- [pytest terminal sonucu](https://github.com/revanseiidov-lab/sinema-bilet-rezervasyon-sistemi/blob/main/evidence/week-01/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%20%E2%80%94%202026-11-05%20%D0%B2%2002.03.29.png)

**Sınırlamalar:** Bu sonuçlar yalnızca iki başlangıç testini kapsar. Kod kapsamı ölçülmedi. Rezervasyon, veritabanı ve güvenlik özellikleri henüz test edilmedi.

**Not:** Terminalde `/favicon.ico` isteği için HTTP 404 ve CSS önbellek isteği için HTTP 304 görülmüştür; bunlar bu iki testin başarısız olduğu anlamına gelmez.
