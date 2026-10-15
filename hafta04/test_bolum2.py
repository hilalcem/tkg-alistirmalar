# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


# 1. Şifre gücü testleri

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"


def test_tek_karakter_sifre_zayif():
    assert sifre_gucu("a") == "zayıf"


def test_7_karakter_sifre_zayif():
    assert sifre_gucu("a" * 7) == "zayıf"


def test_8_karakter_sifre_orta():
    assert sifre_gucu("a" * 8) == "orta"


def test_11_karakter_sifre_orta():
    assert sifre_gucu("a" * 11) == "orta"


def test_12_karakter_sifre_guclu():
    assert sifre_gucu("a" * 12) == "güçlü"


def test_uzun_sifre_guclu():
    assert sifre_gucu("a" * 20) == "güçlü"


def test_bos_sifre_hata():
    with pytest.raises(ValueError):
        sifre_gucu("")


# 2. Otopark ücreti testleri

def test_0_dakika_ucretsiz():
    assert otopark_ucreti(0) == 0


def test_15_dakika_ucretsiz():
    assert otopark_ucreti(15) == 0


def test_16_dakika_20_tl():
    assert otopark_ucreti(16) == 20


def test_60_dakika_20_tl():
    assert otopark_ucreti(60) == 20


def test_61_dakika_40_tl():
    assert otopark_ucreti(61) == 40


def test_180_dakika_40_tl():
    assert otopark_ucreti(180) == 40


def test_181_dakika_60_tl():
    assert otopark_ucreti(181) == 60


def test_uzun_sure_60_tl():
    assert otopark_ucreti(300) == 60


def test_negatif_dakika_hata():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


# 3. Yüzde değişim testleri

def test_yuzde_artis():
    assert yuzde_degisim(200, 250) == pytest.approx(25.0)


def test_yuzde_azalis():
    assert yuzde_degisim(200, 150) == pytest.approx(-25.0)


def test_deger_degismemis():
    assert yuzde_degisim(200, 200) == pytest.approx(0.0)


def test_yeni_deger_sifir():
    assert yuzde_degisim(200, 0) == pytest.approx(-100.0)


def test_yuzde_100_artis():
    assert yuzde_degisim(100, 200) == pytest.approx(100.0)


def test_kesirli_yuzde():
    assert yuzde_degisim(3, 4) == pytest.approx(100 / 3)


def test_eski_deger_sifir_hata():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)


def test_iki_deger_de_sifir_hata():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 0)