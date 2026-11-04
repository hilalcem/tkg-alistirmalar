# Alıştırma 5: Statik Analiz

Bu hafta `alistirma.py` içindeki kod **çalışıyor ama kötü yazılmış**: kullanılmayan importlar, PEP 8'e uymayan adlar, `== None`, gereksiz yere iç içe `if`'ler...
Sizin işiniz kodu **temizlemek**. Fonksiyonların adlarını ve ne yaptıklarını değiştirmiyorsunuz; yalnızca nasıl yazıldıklarını.

Rehber: ders notlarındaki **Statik Test 101** sayfası.

## Dosyalar

| Dosya | Ne yapacaksınız? |
|---|---|
| `alistirma.py` | **Düzenleyeceğiniz dosya.** Her fonksiyonun üstünde ne yapması gerektiği yazıyor. |
| `test_alistirma.py` | **Değiştirmeyin.** Fonksiyonların doğru çalışıp çalışmadığını kontrol eder. |
| `test_stil.py` | **Değiştirmeyin.** `alistirma.py`'yi ruff ile kontrol eder. |
| `ruff.toml` | **Değiştirmeyin.** Bu haftanın ruff ayarları. |
| `requirements.txt` | Bu haftanın ek paketi: `ruff`. |

## İlk kurulum

```bash
cd hafta06
python -m pip install -r requirements.txt
```

## Kodunuz nasıl ölçülüyor?

Üç şeyin hepsi yeşil olmalı:

1. **`ruff check` temiz** (`test_stil.py`): hiçbir uyarı kalmamalı.
2. **`ruff format` temiz** (`test_stil.py`): dosya zaten biçimlendirilmiş olmalı.
3. **Davranış aynı** (`test_alistirma.py`): temizlerken bir şeyi bozmadığınızı bu testler gösterir.

Başta `test_alistirma.py`'deki testlerden **biri kırmızı**. Kod çalışıyor gibi görünse de içinde gerçek bir hata var. Ruff'ın uyarılarından biri size nedenini söylüyor.

## Çalıştırmak

```bash
python -m pytest -v
```

Ruff'ı kendiniz çalıştırmak için (bu klasörde):

```bash
python -m ruff check alistirma.py
python -m ruff format alistirma.py
```

Bir uyarının ne demek olduğunu öğrenmek için kodunu yazın: `python -m ruff rule B006`

## İpuçları

- Önce `python -m ruff format alistirma.py` çalıştırın; boşluk ve tırnak gibi biçim sorunları kendiliğinden düzelir.
- Sonra `python -m ruff check --fix alistirma.py`: güvenli düzeltmeleri ruff kendisi yapar. Kalanları siz düzeltirsiniz.
- Bir adı değiştirdiyseniz (ör. `NotListesi` → `notlar`) fonksiyonun içindeki **her** kullanımını da değiştirin; yoksa `F821 Undefined name` görürsünüz.
- Her değişiklikten sonra `python -m pytest -v` çalıştırın. Testler kırmızıya dönerse son değişikliğiniz davranışı bozmuştur.
- `# noqa` ile uyarı susturmak işe yaramaz; test bu yorumları yok sayar.
