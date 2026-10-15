# Bu dosyayı DEĞİŞTİRMEYİN.
#
# alistirma.py'nin içine bilerek tek bir hata konmuş sürümler üretir ve sizin
# testlerinizi (test_alistirma.py) her birine karşı ayrı ayrı çalıştırır.
# İyi testler, hatalı her sürümde en az bir kez başarısız olmalıdır.
# Bir satır kırmızıysa: testleriniz o hatayı fark etmiyor demektir.

import pathlib
import shutil
import subprocess
import sys

import pytest

KLASOR = pathlib.Path(__file__).parent

# (kimlik, doğru satır, hatalı satır, ipucu)
HATALI_SURUMLER = [
    ("indirim-1", "if tutar < 100:", "if tutar <= 100:",
     "indirim_orani: 100 TL sınırı"),
    ("indirim-2", "if tutar < 500:", "if tutar <= 500:",
     "indirim_orani: 500 TL sınırı"),
    ("indirim-3", "if tutar < 1000:", "if tutar <= 1000:",
     "indirim_orani: 1000 TL sınırı"),
    ("indirim-4", 'raise ValueError("tutar negatif olamaz")', "return 0",
     "indirim_orani: negatif tutarda ne olmalı?"),
    ("sepet-1", 'toplam = toplam + urun["fiyat"] * urun["adet"]', 'toplam = toplam + urun["fiyat"]',
     "sepet_toplami: adedi 1'den fazla olan bir ürün denediniz mi?"),
    ("sepet-2", 'if urun["adet"] <= 0:', 'if urun["adet"] < 0:',
     "sepet_toplami: adedi tam 0 olan ürün"),
    ("pahali-1", 'if urun["fiyat"] > en_pahali["fiyat"]:', 'if urun["fiyat"] >= en_pahali["fiyat"]:',
     "en_pahali_urun: aynı en yüksek fiyatta iki ürün olursa hangisi dönmeli?"),
    ("pahali-2", "return None", 'return ""',
     "en_pahali_urun: boş sepette tam olarak ne dönmeli?"),
]


@pytest.mark.parametrize(
    "dogru, hatali, ipucu",
    [h[1:] for h in HATALI_SURUMLER],
    ids=[h[0] for h in HATALI_SURUMLER],
)
def test_hatali_surum_yakalanmali(dogru, hatali, ipucu, tmp_path):
    kaynak = (KLASOR / "alistirma.py").read_text(encoding="utf-8")
    if kaynak.count(dogru) != 1:
        pytest.fail("alistirma.py değiştirilmiş; dosyayı eski haline getirin.", pytrace=False)

    (tmp_path / "alistirma.py").write_text(kaynak.replace(dogru, hatali), encoding="utf-8")
    shutil.copy(KLASOR / "test_alistirma.py", tmp_path)
    sonuc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_alistirma.py"],
        cwd=tmp_path, capture_output=True, text=True,
    )

    if sonuc.returncode == 5:
        pytest.fail("test_alistirma.py içinde hiç test bulunamadı.", pytrace=False)
    if sonuc.returncode != 1:
        pytest.fail(f"Testleriniz bu hatalı sürümü yakalayamadı. İpucu: {ipucu}", pytrace=False)
