# Hafta 3: Bu dosyadaki kod DOĞRU çalışıyor. Bu dosyayı DEĞİŞTİRMEYİN.
#
# Sizin işiniz bu fonksiyonların testlerini test_alistirma.py dosyasına yazmak.
# Her fonksiyonun üstündeki açıklama, fonksiyonun ne yapması gerektiğini (şartnameyi) anlatıyor.
# Testlerinizi koda değil, bu açıklamalara bakarak yazın.


# 1. Kargo ücreti
# - Sipariş tutarı 500 TL veya üzeriyse kargo ücretsizdir: 0 döndürür.
# - 500 TL'nin altındaysa kargo ücreti 50 TL'dir: 50 döndürür.
# - Tutar negatifse ValueError fırlatır.
def kargo_ucreti(tutar):
    if tutar < 0:
        raise ValueError("tutar negatif olamaz")
    if tutar >= 500:
        return 0
    return 50


# 2. Müze bileti
# - 0-6 yaş arası ücretsiz: 0
# - 7-17 yaş arası öğrenci bileti: 50
# - 18-64 yaş arası tam bilet: 100
# - 65 yaş ve üzeri: 60
# - Yaş negatifse ValueError fırlatır.
def bilet_fiyati(yas):
    if yas < 0:
        raise ValueError("yaş negatif olamaz")
    if yas <= 6:
        return 0
    if yas <= 17:
        return 50
    if yas >= 65:
        return 60
    return 100


# 3. Not ortalaması
# - Listedeki notların ortalamasını döndürür (ör. [70, 85] için 77.5).
# - Liste boşsa ValueError fırlatır.
def ortalama(notlar):
    if len(notlar) == 0:
        raise ValueError("liste boş")
    return sum(notlar) / len(notlar)
