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
    pass


# 2. Asal sayı mı?
# - n'nin 1'den ve kendisinden başka böleni yoksa True döndürür.
# - 0 ve 1 asal değildir; 2 asaldır.
# Örnek: asal_mi(7) -> True, asal_mi(9) -> False
def asal_mi(n):
    pass


# 3. Palindrom mu?
# - Metin tersten okununca da aynıysa True döndürür.
# - Büyük/küçük harf ve boşluklar önemsenmez.
# İpucu: metin.lower() küçük harfe çevirir, metin.replace(" ", "") boşlukları siler.
# Örnek: palindrom_mu("Kek") -> True, palindrom_mu("Ey Edip Adanada pide ye") -> True
def palindrom_mu(metin):
    pass


# 4. En uzun kelime
# - Cümledeki en uzun kelimeyi döndürür.
# - Aynı uzunlukta birden fazla kelime varsa önce geleni döndürür.
# - Cümle boşsa "" (boş metin) döndürür.
# İpucu: cumle.split() cümleyi kelimelerin listesine böler.
# Örnek: en_uzun_kelime("bugün hava çok güzel") -> "bugün"
def en_uzun_kelime(cumle):
    pass


# 5. En düşük not (HATALI: bulun ve düzeltin)
# - Listedeki en küçük notu döndürür.
# - Liste boşsa None döndürür.
def en_dusuk_not(notlar):
    if len(notlar) == 0:
        return None
    en_dusuk = 0
    for n in notlar:
        if n < en_dusuk:
            en_dusuk = n
    return en_dusuk


# 6. 1'den n'ye kadar toplam (HATALI: bulun ve düzeltin)
# - 1 + 2 + ... + n toplamını döndürür. n 0 ise 0 döndürür.
# Örnek: toplam(5) -> 15
def toplam(n):
    sonuc = 0
    for i in range(1, n):
        sonuc = sonuc + i
    return sonuc
