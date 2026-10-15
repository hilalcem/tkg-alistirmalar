# Alıştırma 4: Kapsam ve parametrize

Geçen haftaki gibi `alistirma.py` içindeki kod **doğru çalışıyor**, siz onun testlerini `test_alistirma.py` dosyasına yazacaksınız.
Üç fonksiyon var: `indirim_orani`, `sepet_toplami`, `en_pahali_urun`.
Testlerinizi kısa tutmak için `@pytest.mark.parametrize` işinize yarayacak.

Rehber: ders notlarındaki **pytest 102** sayfası.

## Dosyalar

| Dosya | Ne yapacaksınız? |
|---|---|
| `alistirma.py` | Okuyun, **değiştirmeyin**. Her fonksiyonun üstünde ne yapması gerektiği yazıyor. |
| `test_alistirma.py` | Testlerinizi buraya yazın. İçinde örnek bir test var. |
| `test_kapsam.py` | **Değiştirmeyin.** Testlerinizin kodun her satırını ve her dalını çalıştırıp çalıştırmadığını ölçer. |
| `test_hatali_surumler.py` | **Değiştirmeyin.** Koda bilerek hata koyar; testlerinizin bu hataları yakalayıp yakalamadığına bakar. |
| `requirements.txt` | Bu haftanın ek paketleri: `pytest-cov`, `hypothesis`. |

## İlk kurulum

```bash
cd hafta05
python -m pip install -r requirements.txt
```

## Testleriniz nasıl ölçülüyor?

Bu hafta iki kontrol var ve ikisi de yeşil olmalı:

1. **Dal kapsamı %100** (`test_kapsam.py`): Her `if`'in hem doğru hem yanlış yolu, her döngünün hem çalıştığı hem hiç çalışmadığı durum en az bir testinizde denenmeli. Kırmızıysa mesaj, `alistirma.py`'nin hangi satırlarının eksik kaldığını söyler.
2. **8 hatalı sürümün hepsi yakalanmalı** (`test_hatali_surumler.py`): Geçen haftaki gibi.

Kapsamı %100 yapmak kolaydır ama tek başına yetmez: her satırı çalıştırıp sonucu kontrol etmeyen bir test de %100 kapsam verir. Hatalı sürümler bunu yakalar.

## Çalıştırmak

```bash
python -m pytest -v
```

Yalnızca kendi testlerinizin kapsamını satır satır görmek için:

```bash
python -m pytest test_alistirma.py --cov=alistirma --cov-branch --cov-report=term-missing
```
