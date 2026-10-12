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
    ("kargo-1", "if tutar >= 500:", "if tutar > 500:",
     "kargo_ucreti: ücretsiz kargo sınırını tam sınırda denediniz mi?"),
    ("kargo-2", "if tutar < 0:", "if tutar <= 0:",
     "kargo_ucreti: 0 TL'lik sipariş geçerli mi?"),
    ("kargo-3", 'raise ValueError("tutar negatif olamaz")', "return 50",
     "kargo_ucreti: negatif tutarda ne olmalı?"),
    ("bilet-1", "if yas <= 6:", "if yas < 6:",
     "bilet_fiyati: ücretsiz bilet sınırı"),
    ("bilet-2", "if yas <= 17:", "if yas <= 18:",
     "bilet_fiyati: öğrenci bileti ile tam bilet arasındaki sınır"),
    ("bilet-3", "if yas >= 65:", "if yas > 65:",
     "bilet_fiyati: 65 yaş sınırı"),
    ("ortalama-1", "return sum(notlar) / len(notlar)", "return sum(notlar) // len(notlar)",
     "ortalama: sonucu tam sayı çıkmayan bir liste denediniz mi?"),
    ("ortalama-2", 'raise ValueError("liste boş")', "return 0",
     "ortalama: boş listede ne olmalı?"),
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
