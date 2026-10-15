# Lab, Bölüm 1: Python. Bu dosyadaki fonksiyonları SİZ yazacaksınız.
#
# Testler test_bolum1.py dosyasında hazır; o dosyayı değiştirmeyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum1.py -v
#
# 1-4: `pass` satırını silip fonksiyonu yazın.
# 5-6: Fonksiyon yazılmış ama içinde bir hata var. Testleri çalıştırın, hatayı bulun ve düzeltin.


# 1. Vize-final sonucu
# - Ortalama = vize × 0.4 + final × 0.6
# - Ortalama 50 veya üstü VE final 50 veya üstüyse "Geçti", değilse "Kaldı" döndürür.
# Örnek: vize_final_sonuc(30, 70) -> "Geçti"   (ortalama 54, final 70)
def vize_final_sonuc(vize, final):
    ortalama = vize * 0.4 + final * 0.6
    if ortalama >= 50 and final >= 50:
        return "Geçti"
    return "Kaldı"



# 2. Asal sayı mı?
# - n'nin 1'den ve kendisinden başka böleni yoksa True döndürür.
# - 0 ve 1 asal değildir; 2 asaldır.
# Örnek: asal_mi(7) -> True, asal_mi(9) -> False
def asal_mi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# 3. Palindrom mu?
# - Metin tersten okununca da aynıysa True döndürür.
# - Büyük/küçük harf ve boşluklar önemsenmez.
# İpucu: metin.lower() küçük harfe çevirir, metin.replace(" ", "") boşlukları siler.
# Örnek: palindrom_mu("Kek") -> True, palindrom_mu("Ey Edip Adanada pide ye") -> True
def palindrom_mu(metin):
    metin = metin.replace(" ", "").lower()
    ters_metin = metin[::-1]
    return metin == ters_metin


# 4. En uzun kelime
# - Cümledeki en uzun kelimeyi döndürür.
# - Aynı uzunlukta birden fazla kelime varsa önce geleni döndürür.
# - Cümle boşsa "" (boş metin) döndürür.
# İpucu: cumle.split() cümleyi kelimelerin listesine böler.
# Örnek: en_uzun_kelime("bugün hava çok güzel") -> "bugün"
def en_uzun_kelime(cumle):
    if len(cumle) == 0:
        return ""
    kelimeler = cumle.split()
    en_uzun = kelimeler[0]
    for kelime in kelimeler:
        if len(kelime) > len(en_uzun):
            en_uzun = kelime
    return en_uzun


# 5. En düşük not (HATALI: bulun ve düzeltin)
# - Listedeki en küçük notu döndürür.
# - Liste boşsa None döndürür.
def en_dusuk_not(notlar):
    if len(notlar) == 0:
        return None
    en_dusuk = notlar[0]
    for n in notlar:
        if n < en_dusuk:
            en_dusuk = n
    return en_dusuk


# 6. 1'den n'ye kadar toplam (HATALI: bulun ve düzeltin)
# - 1 + 2 + ... + n toplamını döndürür. n 0 ise 0 döndürür.
# Örnek: toplam(5) -> 15
def toplam(n):
    sonuc = 0
    for i in range(1, n + 1):
        sonuc = sonuc + i
    return sonuc
