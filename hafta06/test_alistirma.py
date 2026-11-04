# Bu dosyayı DEĞİŞTİRMEYİN.
#
# alistirma.py'deki fonksiyonların doğru çalışıp çalışmadığını kontrol eder.
# Kodu temizlerken bu testler yeşil kalmalı: temizlik davranışı değiştirmemeli.

import pytest

from alistirma import (
    bilet_fiyati,
    gecti_mi,
    katilimci_ekle,
    not_ortalamasi,
    ortalama_metni,
    sayiya_cevir,
)


@pytest.mark.parametrize(
    "yas, ogrenci, hafta_sonu, beklenen",
    [
        (0, False, False, 0),
        (5, True, True, 0),
        (6, False, False, 100),
        (6, True, False, 70),
        (30, False, True, 150),
        (20, True, True, 120),
    ],
)
def test_bilet_fiyati(yas, ogrenci, hafta_sonu, beklenen):
    assert bilet_fiyati(yas, ogrenci, hafta_sonu) == beklenen


def test_negatif_yas_hata_verir():
    with pytest.raises(ValueError):
        bilet_fiyati(-1, False, False)


def test_not_ortalamasi():
    assert not_ortalamasi([70, 80, 90]) == 80
    assert not_ortalamasi([50]) == 50
    assert not_ortalamasi([1, 2]) == pytest.approx(1.5)


def test_bos_listenin_ortalamasi_yok():
    assert not_ortalamasi([]) is None


@pytest.mark.parametrize(
    "notlar, beklenen",
    [
        ([70, 75], "72.5"),
        ([100], "100.0"),
        ([60, 70, 70], "66.7"),
        ([0], "0.0"),
        ([], "not yok"),
    ],
    ids=["iki not", "tek not", "yuvarlama", "sifir", "bos liste"],
)
def test_ortalama_metni(notlar, beklenen):
    assert ortalama_metni(notlar) == beklenen


@pytest.mark.parametrize(
    "puan, beklenen",
    [(100, True), (50, True), (49, False), (0, False)],
)
def test_gecti_mi(puan, beklenen):
    assert gecti_mi(puan) is beklenen


@pytest.mark.parametrize(
    "metin, beklenen",
    [("42", 42), ("-7", -7), ("abc", None), ("", None), ("3.5", None)],
)
def test_sayiya_cevir(metin, beklenen):
    assert sayiya_cevir(metin) == beklenen


def test_katilimci_verilen_listeye_eklenir():
    assert katilimci_ekle("Can", ["Ali", "Ayşe"]) == ["Ali", "Ayşe", "Can"]


def test_liste_verilmezse_her_seferinde_yeni_liste():
    assert katilimci_ekle("Ali") == ["Ali"]
    assert katilimci_ekle("Ayşe") == ["Ayşe"]
