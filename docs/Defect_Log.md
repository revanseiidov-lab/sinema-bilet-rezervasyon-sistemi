# Hata Kayıtları

| Kimlik | Bulgu | Düzeltme ve doğrulama | Durum |
| --- | --- | --- | --- |
| DEF-W02-01 | İç içe iki depo kopyası nedeniyle dış klasörde pytest aynı adlı test modüllerini topladı. | Geliştirme iç kopyada yürütüldü. Proje köküne `testpaths = tests` eklendi. Tam paket toplandı. | Proje kökünde doğrulandı |
| DEF-W02-02 | İlk Hafta 02 çalıştırmasında CLI için bir test başarısız oldu. Flask uygulama bağlamı eksikti. | `with_appcontext` eklendi. CLI testi ve tam paket tekrar çalıştırıldı. | Düzeltildi |
