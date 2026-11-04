# Alıştırma 5: Bu dosyadaki kod ÇALIŞIYOR ama kötü yazılmış.
#
# Sizin işiniz kodu temizlemek:
#   - ruff check hiçbir sorun bulmamalı,
#   - ruff format dosyayı değiştirmemeli,
#   - test_alistirma.py'deki testlerin hepsi geçmeli.
# Fonksiyonların adlarını ve ne yaptıklarını değiştirmeyin; yalnızca nasıl
# yazıldıklarını değiştirin. Her fonksiyonun üstündeki açıklama, ne yapması
# gerektiğini (şartnameyi) anlatıyor.
import os
import math
import sys


# 1. Bilet fiyatı
# - Yaş negatifse ValueError fırlatır.
# - 6 yaşından küçükler ücretsizdir (0 TL).
# - Hafta içi bilet 100 TL, hafta sonu 150 TL.
# - Öğrencilere 30 TL indirim yapılır.
def bilet_fiyati(yas, ogrenci, hafta_sonu):
    if yas < 0:
        raise ValueError('yaş negatif olamaz')
    if yas < 6:
        return 0
    if hafta_sonu == True:
        if ogrenci == True:
            return 120
        else:
            return 150
    else:
        if ogrenci == True:
            return 70
        else:
            return 100


# 2. Not ortalaması
# - Notların ortalamasını döndürür.
# - Liste boşsa None döndürür.
def not_ortalamasi(NotListesi):
    if len(NotListesi)==0:
        return None
    Toplam=0
    for i in range(len(NotListesi)):
        Toplam = Toplam+NotListesi[i]
    sonuc = Toplam / len(NotListesi)
    return Toplam / len(NotListesi)


# 3. Ortalama metni
# - Not listesi boşsa "not yok" döndürür.
# - Değilse ortalamayı bir ondalık basamağa yuvarlayıp metin olarak döndürür.
def ortalama_metni(notlar):
    ort = not_ortalamasi(notlar)
    if ort == None:
        return 'not yok'
    return str(round(ort, 1))
# 4. Geçti mi?
# - Puan 50 veya üstüyse True, değilse False döndürür.
def gecti_mi(puan):
    if puan >= 50:   
        return True
    else:
        return False


# 5. Sayıya çevir
# - Metni tam sayıya çevirip döndürür: "42" -> 42
# - Metin bir tam sayı değilse None döndürür: "abc" -> None
def sayiya_cevir(metin):
    try:
        return int(metin)
    except:
        return None


# 6. Katılımcı ekle
# - Adı listenin sonuna ekler ve listeyi döndürür.
# - Liste verilmezse yeni, boş bir listeye ekler.
def katilimci_ekle(ad, liste=[]):
    liste.append(ad)
    return liste
