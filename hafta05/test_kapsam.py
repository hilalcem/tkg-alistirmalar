# Bu dosyayı DEĞİŞTİRMEYİN.
#
# Testlerinizin (test_alistirma.py) alistirma.py'nin her satırını ve her dalını
# çalıştırıp çalıştırmadığını ölçer. Dal: bir if'in hem doğru hem yanlış yolu,
# bir döngünün hem en az bir kez dönmesi hem hiç dönmeden geçilmesi.
# Hedef: %100 dal kapsamı (branch coverage).

import json
import os
import pathlib
import subprocess
import sys

import pytest

KLASOR = pathlib.Path(__file__).parent


def test_dal_kapsami_yuzde_yuz(tmp_path):
    try:
        import pytest_cov  # noqa: F401
    except ImportError:
        pytest.fail("pytest-cov kurulu değil. Bu klasörde: python -m pip install -r requirements.txt",
                    pytrace=False)

    rapor = tmp_path / "kapsam.json"
    sonuc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider", "test_alistirma.py",
         "--cov=alistirma", "--cov-branch", f"--cov-report=json:{rapor}"],
        cwd=KLASOR, capture_output=True, text=True,
        env={**os.environ, "COVERAGE_FILE": str(tmp_path / ".coverage")},
    )
    if not rapor.exists():
        pytest.fail("Kapsam ölçülemedi. pytest çıktısı:\n" + sonuc.stdout[-1500:], pytrace=False)

    dosya = json.loads(rapor.read_text(encoding="utf-8"))["files"]["alistirma.py"]
    yuzde = dosya["summary"]["percent_covered"]
    if yuzde < 100:
        mesaj = [f"Dal kapsamı %{yuzde:.0f}, hedef %100."]
        if dosya["missing_lines"]:
            mesaj.append("Hiç çalışmayan satırlar: " + ", ".join(map(str, dosya["missing_lines"])))
        if dosya["missing_branches"]:
            satirlar = sorted({baslangic for baslangic, _ in dosya["missing_branches"]})
            mesaj.append("Bir yolu hiç denenmemiş koşul/döngü satırları: " + ", ".join(map(str, satirlar)))
        mesaj.append("Satır numaraları alistirma.py dosyasına göre.")
        pytest.fail("\n".join(mesaj), pytrace=False)
