# Alıştırma 3: Lab — Python ve test

Bu lab, şimdiye kadar gördüğümüz her şeyi bir arada kullanıyor: Python temelleri (fonksiyon, if, döngü, liste, metin) ve test yazmak (`assert`, pytest, `pytest.raises`, `pytest.approx`, sınır değerleri).
İki bölümden oluşuyor. Kendi hızınızda, sırayla ilerleyin.

| Bölüm | Sizin işiniz | Düzenleyeceğiniz dosya | Kontrol eden |
|---|---|---|---|
| 1. Python | 4 fonksiyon yazın, 2 hatalı fonksiyonu düzeltin | `bolum1.py` | `test_bolum1.py` (hazır) |
| 2. Test | Hazır kodun testlerini yazın | `test_bolum2.py` | `test_hatali_surumler.py` (hazır) |

`test_bolum1.py`, `bolum2.py` ve `test_hatali_surumler.py` dosyalarını **değiştirmeyin**.

Takıldığınızda ders notlarındaki rehberlere bakın: **Python 101** (Bölüm 1 için) ve **pytest 101** (Bölüm 2 için).

## Başlamadan önce

1. Elinizdeki değişiklikleri commit'leyip push edin. Sonra GitHub'da kendi fork'unuzda **Sync fork → Update branch** düğmesine basın.
2. Bilgisayarınızda yeni haftayı alın ve klasöre girin:
   ```bash
   git pull
   cd hafta04
   ```

## Bölüm 1: Python

`bolum1.py` dosyasını açın. Her fonksiyonun üstünde ne yapması gerektiği ve bir örnek yazıyor.

1. Testleri çalıştırın. Başta hepsi kırmızı:
   ```bash
   python -m pytest test_bolum1.py -v
   ```
2. Fonksiyonları **tek tek** yazın. Her birinden sonra testleri tekrar çalıştırın ve o fonksiyonun satırının yeşile döndüğünü görün.
3. 5 ve 6 numaralı fonksiyonlar yazılmış ama hatalı. Test çıktısında hangi değerin beklendiğini ve ne geldiğini okuyun (`assert 0 == 45` gibi), sonra kodda hatanın nerede olduğunu bulun.

| Fonksiyon | Kullanacağınız şeyler | Python 101'de |
|---|---|---|
| `vize_final_sonuc` | aritmetik, `and`, `if` | 4, 7, 8. bölümler |
| `asal_mi` | `for`, `range`, `%` | 4, 9. bölümler |
| `palindrom_mu` | metin işlemleri, döngü ya da dilimleme | 5, 9. bölümler |
| `en_uzun_kelime` | liste üzerinde dolaşmak, `len` | 12. bölüm |
| `en_dusuk_not` (hatalı) | döngüde başlangıç değeri | 12. bölüm |
| `toplam` (hatalı) | `range`'in bitiş değeri | 9. bölüm |

## Bölüm 2: Test

`bolum2.py` dosyasındaki üç fonksiyon **doğru** çalışıyor: `sifre_gucu`, `otopark_ucreti`, `yuzde_degisim`. Siz bunların testlerini `test_bolum2.py` dosyasına yazacaksınız.

1. Her fonksiyonun açıklamasından bir tablo çıkarın: hangi gruplar var, sınırlar nerede? Örneğin `otopark_ucreti` için 15, 16, 60, 61, ... (pytest 101, 8. bölüm)
2. Her grup ve her sınır için test yazın. Hata fırlatması gereken durumlar için `pytest.raises` (9. bölüm), ondalıklı sonuçlar için `pytest.approx` (10. bölüm) kullanın.
3. Çalıştırın:
   ```bash
   python -m pytest test_bolum2.py test_hatali_surumler.py -v
   ```

`test_hatali_surumler.py`, `bolum2.py`'ye bilerek hata koyarak 9 bozuk sürüm üretir ve testlerinizi her birine karşı çalıştırır (pytest 101, 12. bölüm). Kırmızı her satırın altında bir ipucu var:

```
Testleriniz bu hatalı sürümü yakalayamadı. İpucu: otopark_ucreti: 15 dakika sınırı
```

Hedef: kendi testlerinizin hepsi geçsin ve 9 bozuk sürümün hepsi yakalansın.

## Bitirince

```bash
python -m pytest -v
git add .
git commit -m "hafta04 lab"
git push
```

Fork'unuzun **Actions** sekmesinde `hafta04` satırı yeşil olmalı. Bitiremediyseniz yaptığınız kadarını yine gönderin; sonra devam edip tekrar push edebilirsiniz.

## Kontrol listesi

- [ ] `test_bolum1.py`'deki 6 testin hepsi yeşil
- [ ] `test_bolum2.py`'de her fonksiyonun her sınırı için test var
- [ ] `test_hatali_surumler.py`'deki 9 satırın hepsi yeşil
- [ ] Push ettim, Actions'ta `hafta04` yeşil
