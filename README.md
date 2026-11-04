# Sinema Bilet Rezervasyon Sistemi

**Ders:** YZM6301 — Yazılım Kalitesi  
**Üniversite:** Beykoz Üniversitesi  
**İsimler:** Revan Seiidov, Fadıl Sebbağ  
**Geliştirme sorumlusu:** Revan Seiidov  
**Durum:** Planlama / başlangıç (prototip henüz tamamlanmadı)

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

## Geliştirme Durumu
Şu anda proje kurulumu ve belge planlaması sürmektedir. Uygulamanın çalıştırılma adımları ilk Flask sürümü tamamlandığında buraya eklenecektir.

## SQA İlkesi
Test sonuçları, hata kayıtları, kod incelemeleri ve kalite metrikleri ancak gerçekten uygulandığında ve kanıtları kaydedildiğinde raporlanacaktır. Haftalık Kanban ekran görüntüleri korunacaktır.
