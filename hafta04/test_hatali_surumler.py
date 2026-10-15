# Bu dosyayı DEĞİŞTİRMEYİN.
#
# bolum2.py'nin içine bilerek tek bir hata konmuş sürümler üretir ve sizin
# testlerinizi (test_bolum2.py) her birine karşı ayrı ayrı çalıştırır.
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
    ("sifre-1", "if len(sifre) < 8:", "if len(sifre) <= 8:",
     "sifre_gucu: zayıf ile orta arasındaki sınır"),
    ("sifre-2", "if len(sifre) < 12:", "if len(sifre) <= 12:",
     "sifre_gucu: orta ile güçlü arasındaki sınır"),
    ("sifre-3", 'raise ValueError("şifre boş olamaz")', 'return "zayıf"',
     "sifre_gucu: boş şifrede ne olmalı?"),
    ("otopark-1", "if dakika <= 15:", "if dakika < 15:",
     "otopark_ucreti: 15 dakika sınırı"),
    ("otopark-2", "if dakika <= 60:", "if dakika < 60:",
     "otopark_ucreti: 60 dakika sınırı"),
    ("otopark-3", "if dakika <= 180:", "if dakika < 180:",
     "otopark_ucreti: 180 dakika sınırı"),
    ("otopark-4", 'raise ValueError("dakika negatif olamaz")', "return 0",
     "otopark_ucreti: negatif dakikada ne olmalı?"),
    ("yuzde-1", "return (yeni - eski) / eski * 100", "return (yeni - eski) / yeni * 100",
     "yuzde_degisim: sonucu şartnamedeki örneklerle karşılaştırdınız mı?"),
    ("yuzde-2", 'raise ValueError("eski değer 0 olamaz")', "return 0",
     "yuzde_degisim: eski değer 0 olursa ne olmalı?"),
]


@pytest.mark.parametrize(
    "dogru, hatali, ipucu",
    [h[1:] for h in HATALI_SURUMLER],
    ids=[h[0] for h in HATALI_SURUMLER],
)
def test_hatali_surum_yakalanmali(dogru, hatali, ipucu, tmp_path):
    kaynak = (KLASOR / "bolum2.py").read_text(encoding="utf-8")
    if kaynak.count(dogru) != 1:
        pytest.fail("bolum2.py değiştirilmiş; dosyayı eski haline getirin.", pytrace=False)

    (tmp_path / "bolum2.py").write_text(kaynak.replace(dogru, hatali), encoding="utf-8")
    shutil.copy(KLASOR / "test_bolum2.py", tmp_path)
    sonuc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_bolum2.py"],
        cwd=tmp_path, capture_output=True, text=True,
    )

    if sonuc.returncode == 5:
        pytest.fail("test_bolum2.py içinde hiç test bulunamadı.", pytrace=False)
    if sonuc.returncode != 1:
        pytest.fail(f"Testleriniz bu hatalı sürümü yakalayamadı. İpucu: {ipucu}", pytrace=False)
