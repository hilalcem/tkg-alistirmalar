# Alıştırma 4: Bu dosyadaki kod DOĞRU çalışıyor. Bu dosyayı DEĞİŞTİRMEYİN.
#
# Sizin işiniz bu fonksiyonların testlerini test_alistirma.py dosyasına yazmak.
# Her fonksiyonun üstündeki açıklama, fonksiyonun ne yapması gerektiğini (şartnameyi) anlatıyor.
# Testlerinizi koda değil, bu açıklamalara bakarak yazın.
#
# Sepet, ürünlerin listesidir. Her ürün bir sözlüktür:
#     {"urun": "çay", "fiyat": 20, "adet": 2}


# 1. İndirim oranı
# Sepet tutarına göre yüzde kaç indirim yapılacağını döndürür:
# - 0-99 TL: 0
# - 100-499 TL: 5
# - 500-999 TL: 10
# - 1000 TL ve üzeri: 15
# - Tutar negatifse ValueError fırlatır.
def indirim_orani(tutar):
    if tutar < 0:
        raise ValueError("tutar negatif olamaz")
    if tutar < 100:
        return 0
    if tutar < 500:
        return 5
    if tutar < 1000:
        return 10
    return 15


# 2. Sepet toplamı
# - Her ürün için fiyat × adet hesaplanır ve hepsi toplanır.
# - Boş sepetin toplamı 0'dır.
# - Adedi 0 veya negatif olan bir ürün varsa ValueError fırlatır.
def sepet_toplami(sepet):
    toplam = 0
    for urun in sepet:
        if urun["adet"] <= 0:
            raise ValueError("adet pozitif olmalı")
        toplam = toplam + urun["fiyat"] * urun["adet"]
    return toplam


# 3. En pahalı ürün
# - Sepetteki birim fiyatı en yüksek ürünün adını döndürür.
# - En yüksek fiyatta birden fazla ürün varsa listede önce geleni döndürür.
# - Sepet boşsa None döndürür.
def en_pahali_urun(sepet):
    if len(sepet) == 0:
        return None
    en_pahali = sepet[0]
    for urun in sepet:
        if urun["fiyat"] > en_pahali["fiyat"]:
            en_pahali = urun
    return en_pahali["urun"]

