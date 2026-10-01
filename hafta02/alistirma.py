# Hafta 2: Python temelleri
#
# Her fonksiyonun içindeki `pass` satırını silip kendi kodunuzu yazın.
# Fonksiyonların adlarını ve parametrelerini DEĞİŞTİRMEYİN; testler bu adlarla çalışır.
# Kendi bilgisayarınızda denemek için:  cd hafta02  ve ardından  python -m pytest -v


# 1. İşaret
# Sayı 0'dan büyükse "pozitif", küçükse "negatif", 0 ise "sıfır" döndürün.
# Örnek: isaret(5) -> "pozitif"
def isaret(sayi):
    if sayi > 0:
        return "pozitif"
    elif sayi < 0:
        return "negatif"
    else:
        return "sıfır"


# 2. Dönem notu
# Vizenin %40'ı ile finalin %60'ını toplayıp döndürün.
# Örnek: donem_notu(50, 70) -> 62.0
def donem_notu(vize, final):
    return (vize * 0.4) + (final * 0.6)


# 3. Harf sayma
# `metin` içinde `harf` karakterinin kaç kez geçtiğini döndürün.
# Büyük/küçük harf ayrımı yapın: "A" ile "a" farklı harflerdir.
# Örnek: harf_say("merhaba", "a") -> 2
def harf_say(metin, harf):
    return metin.count(harf)


# 4. Faktöriyel
# n! = 1 * 2 * 3 * ... * n değerini bir döngüyle hesaplayın. 0! = 1'dir.
# Örnek: faktoriyel(5) -> 120
def faktoriyel(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# 5. Geçenler
# Nottan 60 ve üzeri olanları, sıralarını bozmadan yeni bir liste olarak döndürün.
# Örnek: gecenler([70, 45, 90]) -> [70, 90]
def gecenler(notlar):
    gecen_notlar = []
    for not_ in notlar:
        if not_ >= 60:
            gecen_notlar.append(not_)
    return gecen_notlar
