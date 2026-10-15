# Lab, Bölüm 1 testleri. Bu dosyayı DEĞİŞTİRMEYİN.

from bolum1 import vize_final_sonuc, asal_mi, palindrom_mu, en_uzun_kelime, en_dusuk_not, toplam


def test_vize_final_sonuc():
    assert vize_final_sonuc(30, 70) == "Geçti"
    assert vize_final_sonuc(50, 50) == "Geçti"     # iki sınır birden
    assert vize_final_sonuc(40, 55) == "Kaldı"     # ortalama 49
    assert vize_final_sonuc(100, 45) == "Kaldı"    # ortalama 67 ama final 50'nin altında
    assert vize_final_sonuc(0, 100) == "Geçti"


def test_asal_mi():
    assert asal_mi(2) == True
    assert asal_mi(3) == True
    assert asal_mi(17) == True
    assert asal_mi(0) == False
    assert asal_mi(1) == False
    assert asal_mi(4) == False
    assert asal_mi(9) == False
    assert asal_mi(25) == False


def test_palindrom_mu():
    assert palindrom_mu("kek") == True
    assert palindrom_mu("Kek") == True
    assert palindrom_mu("Ey Edip Adanada pide ye") == True
    assert palindrom_mu("araba") == False
    assert palindrom_mu("a") == True


def test_en_uzun_kelime():
    assert en_uzun_kelime("bugün hava çok güzel") == "bugün"
    assert en_uzun_kelime("yazılım testi") == "yazılım"
    assert en_uzun_kelime("bir iki üç") == "bir"       # eşitlikte önce gelen
    assert en_uzun_kelime("merhaba") == "merhaba"
    assert en_uzun_kelime("") == ""


def test_en_dusuk_not():
    assert en_dusuk_not([70, 45, 90]) == 45
    assert en_dusuk_not([100]) == 100
    assert en_dusuk_not([0, 50]) == 0
    assert en_dusuk_not([]) == None


def test_toplam():
    assert toplam(5) == 15
    assert toplam(1) == 1
    assert toplam(0) == 0
    assert toplam(100) == 5050
