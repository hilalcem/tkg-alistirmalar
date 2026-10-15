# Lab, Bölüm 2: Test. Bu dosyadaki kod DOĞRU çalışıyor. Bu dosyayı DEĞİŞTİRMEYİN.
#
# Sizin işiniz bu fonksiyonların testlerini test_bolum2.py dosyasına yazmak.
# Her fonksiyonun üstündeki açıklama şartnamedir; testlerinizi koda değil, ona bakarak yazın.


# 1. Şifre gücü
# - 0-7 karakter: "zayıf"
# - 8-11 karakter: "orta"
# - 12 ve daha fazla karakter: "güçlü"
# - Şifre boşsa ValueError fırlatır.
def sifre_gucu(sifre):
    if len(sifre) == 0:
        raise ValueError("şifre boş olamaz")
    if len(sifre) < 8:
        return "zayıf"
    if len(sifre) < 12:
        return "orta"
    return "güçlü"


# 2. Otopark ücreti
# - 0-15 dakika: 0 TL
# - 16-60 dakika: 20 TL
# - 61-180 dakika: 40 TL
# - 180 dakikadan fazla: 60 TL
# - Dakika negatifse ValueError fırlatır.
def otopark_ucreti(dakika):
    if dakika < 0:
        raise ValueError("dakika negatif olamaz")
    if dakika <= 15:
        return 0
    if dakika <= 60:
        return 20
    if dakika <= 180:
        return 40
    return 60


# 3. Yüzde değişim
# - Eski değerden yeni değere yüzde kaç değişim olduğunu döndürür: (yeni - eski) / eski × 100
#   Örnek: 200'den 250'ye %25 artış -> 25.0, 200'den 150'ye %25 azalış -> -25.0
# - Eski değer 0 ise ValueError fırlatır.
def yuzde_degisim(eski, yeni):
    if eski == 0:
        raise ValueError("eski değer 0 olamaz")
    return (yeni - eski) / eski * 100
