# Hafta 3: Testleri siz yazın

Geçen hafta testler hazırdı, kodu siz yazdınız. Bu hafta tersi:
`alistirma.py` içindeki kod **doğru çalışıyor**, siz onun testlerini `test_alistirma.py` dosyasına yazacaksınız.

Rehber: ders notlarındaki **pytest 101** sayfası.

## Dosyalar

| Dosya | Ne yapacaksınız? |
|---|---|
| `alistirma.py` | Okuyun, **değiştirmeyin**. Her fonksiyonun üstünde ne yapması gerektiği yazıyor. |
| `test_alistirma.py` | Testlerinizi buraya yazın. |
| `test_hatali_surumler.py` | Okuyabilirsiniz, **değiştirmeyin**. Testlerinizin kalitesini ölçer. |

## Testleriniz nasıl ölçülüyor?

`test_hatali_surumler.py`, `alistirma.py`'nin içine bilerek **tek bir hata** koyarak 8 farklı bozuk sürüm üretir.
Sonra sizin testlerinizi her bozuk sürüme karşı ayrı ayrı çalıştırır.

- Testleriniz bozuk sürümde **başarısız olursa**: hatayı yakaladınız ✅
- Testleriniz bozuk sürümde de **geçerse**: hatayı fark etmediniz ❌

Bir hafta yeşil olsun diye iki şey gerekiyor:

1. Testlerinizin hepsi doğru kodda geçmeli.
2. 8 bozuk sürümün hepsi en az bir testinizde yakalanmalı.

## Çalıştırmak

```bash
cd hafta03
python -m pytest -v
```

Başta çıktı şöyle olacak: örnek test geçer, 8 bozuk sürümün hiçbiri yakalanmaz.

```
test_alistirma.py::test_kargo_buyuk_sipariste_ucretsiz PASSED
test_hatali_surumler.py::test_hatali_surum_yakalanmali[kargo-1] FAILED
...
Testleriniz bu hatalı sürümü yakalayamadı. İpucu: kargo_ucreti: ücretsiz kargo sınırını tam sınırda denediniz mi?
```

Her kırmızı satırın altındaki ipucunu okuyun ve o durumu deneyen bir test ekleyin.

## İpuçları

- Her fonksiyon için sıradan değerleri, **tam sınırları** ve **sınırın bir altını/üstünü** deneyin.
- Hata fırlatması gereken durumlar için `pytest.raises` kullanın.
- Her test fonksiyonunun adı `test_` ile başlamalı, yoksa pytest onu görmez.
