# Bu dosyayı DEĞİŞTİRMEYİN.
#
# alistirma.py'yi ruff ile kontrol eder:
#   1. ruff check: PEP 8 ve sık yapılan hatalar için hiçbir uyarı kalmamalı.
#   2. ruff format: dosya zaten biçimlendirilmiş olmalı.
# Ayarlar ruff.toml ile aynıdır.
# Uyarıları noqa yorumuyla susturmak burada işe yaramaz.

import importlib.util
import pathlib
import subprocess
import sys

import pytest

KLASOR = pathlib.Path(__file__).parent
AYARLAR = [
    "--isolated",
    "--line-length=88",
    "--config=lint.select = ['E', 'W', 'F', 'B', 'N', 'SIM', 'C90', 'I']",
    "--config=lint.mccabe.max-complexity = 5",
]


def ruff(*argumanlar):
    if importlib.util.find_spec("ruff") is None:
        pytest.fail(
            "ruff kurulu değil. Bu klasörde: python -m pip install -r requirements.txt",
            pytrace=False,
        )
    return subprocess.run(
        [sys.executable, "-m", "ruff", *argumanlar, *AYARLAR, "alistirma.py"],
        cwd=KLASOR,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def test_ruff_check_temiz():
    sonuc = ruff("check", "--ignore-noqa", "--output-format=concise", "--no-cache")
    if sonuc.returncode != 0:
        pytest.fail(
            "ruff check sorun buldu:\n" + sonuc.stdout + sonuc.stderr, pytrace=False
        )


def test_ruff_format_temiz():
    kaynak = (KLASOR / "alistirma.py").read_text(encoding="utf-8")
    if "fmt:" in kaynak:
        pytest.fail("alistirma.py'de '# fmt:' yorumu var; kaldırın.", pytrace=False)
    sonuc = ruff("format", "--check", "--diff", "--no-cache")
    if sonuc.returncode != 0:
        pytest.fail(
            "alistirma.py biçimlendirilmemiş. Düzeltmek için:\n"
            "    ruff format alistirma.py\n" + sonuc.stdout,
            pytrace=False,
        )
