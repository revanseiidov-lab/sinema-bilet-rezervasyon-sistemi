# Sinema Bilet Rezervasyon Sistemi

**Ders:** YZM6301 — Yazılım Kalitesi  
**Üniversite:** Beykoz Üniversitesi  
**İsimler:** Revan Seiidov, Fadıl Sebbağ  
**Geliştirme sorumlusu:** Revan Seiidov  
**Durum:** Hafta 02: SQLite film kataloğu kullanılabilir. Seans ve rezervasyon sonraki haftalarda geliştirilecek.

## Proje Hakkında
Bu proje, kullanıcıların filmleri ve seansları görüntüleyebileceği, uygun koltukları seçebileceği ve rezervasyon oluşturabileceği küçük ölçekli bir web uygulaması prototipidir.

**Planlanan teknolojiler:** Python, Flask, SQLite, HTML, CSS, pytest.

## Proje Takibi
- [8 haftalık Kanban panosu (GitHub Projects)](https://github.com/users/revanseiidov-lab/projects/1/views/1)
- [DEV / DOC / SQA iş listesi (GitHub Issues)](https://github.com/revanseiidov-lab/sinema-bilet-rezervasyon-sistemi/issues)
- [Proje tanım belgesi](docs/Project_Definition.txt)
- [Kanban ve haftalık teslim yönergesi](docs/Kanban_Haftalik_Takip.md)

## Planlanan Temel Fonksiyonlar
1. Film listesi
2. Seans listesi
3. Koltuk durumlarını görüntüleme
4. Rezervasyon oluşturma ve onay kodu üretme
5. Aynı seans ve koltuk için birden fazla aktif rezervasyonu engelleme

> Bu liste planlanan kapsamdır; tamamlanmış özellik iddiası değildir.

## Planlanan Proje Yapısı
```text
sinema-bilet-rezervasyon-sistemi/
├── app/                 # Flask uygulama modülleri (planlanan)
├── templates/           # HTML sayfaları (planlanan)
├── static/              # CSS ve görseller (planlanan)
├── tests/               # Otomatik testler
├── docs/                # SRS, SDD, SQAP, test ve kalite belgeleri
├── requirements.txt
└── README.md
```

## Kurulum ve Çalıştırma (macOS / Linux)

Python 3.9 veya üzeri ve Git gereklidir.

```bash
git clone https://github.com/revanseiidov-lab/sinema-bilet-rezervasyon-sistemi.git
cd sinema-bilet-rezervasyon-sistemi
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m flask --app app init-db
python3 -m flask --app app run
```

Tarayıcıda http://127.0.0.1:5000 adresini açın ve **Filmleri Gör** bağlantısını seçin. Başlangıç komutu altı kurgusal film ekler. Yeniden çalıştırıldığında mevcut kayıtları değiştirmez veya çoğaltmaz. Yerel veritabanı `instance/cinema.sqlite3` dosyasında tutulur. Sunucuyu durdurmak için terminalde Control+C tuşlarına basın.

Testleri çalıştırmak için:

```bash
python3 -m pytest -v
```

**Hafta 01 doğrulaması:** 05.11.2026 tarihinde macOS / Python 3.9.6 / pytest 8.4.2 ortamında iki test başarıyla çalıştırıldı (2 PASS, 0 FAIL). Bu sonuç sadece başlangıç ana sayfasını kapsar.

- [Hafta 01 test raporu](docs/Test_Results_Week_01.md)
- [Hafta 01 ekran görüntüleri](evidence/week-01/)

## Mevcut Proje Yapısı

```text
app.py
db.py
schema.sql
static/style.css
templates/
tests/
docs/
evidence/week-01/
requirements.txt
README.md
```

Hafta 02 için [ilerleme raporu](docs/Weekly_Progress_Week_02.md), [test raporu](docs/Test_Results_Week_02.md) ve [kanıtlar](evidence/week-02/) mevcuttur.

## SQA İlkesi
Test sonuçları, hata kayıtları, kod incelemeleri ve kalite metrikleri ancak gerçekten uygulandığında ve kanıtları kaydedildiğinde raporlanacaktır. Haftalık Kanban ekran görüntüleri korunacaktır.
