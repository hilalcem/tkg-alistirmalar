import pytest
from alistirma import indirim_orani, sepet_toplami, en_pahali_urun

# 1. indirim_orani testleri
@pytest.mark.parametrize("tutar, beklenen", [
    (0, 0),
    (99, 0),
    (100, 5),    # indirim-1 hatasını yakalar
    (499, 5),
    (500, 10),   # indirim-2 hatasını yakalar
    (999, 10),
    (1000, 15),  # indirim-3 hatasını yakalar
    (5000, 15)
])
def test_indirim_orani_gecerli(tutar, beklenen):
    assert indirim_orani(tutar) == beklenen

def test_indirim_orani_negatif():
    # indirim-4 hatasını yakalar
    with pytest.raises(ValueError, match="tutar negatif olamaz"):
        indirim_orani(-10)


# 2. sepet_toplami testleri
@pytest.mark.parametrize("sepet, beklenen", [
    ([], 0),  # Boş sepet (döngünün hiç çalışmadığı dal)
    ([{"urun": "çay", "fiyat": 20, "adet": 2}], 40),  # sepet-1 hatasını yakalar (adet > 1)
    ([
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ], 145)
])
def test_sepet_toplami_gecerli(sepet, beklenen):
    assert sepet_toplami(sepet) == beklenen

@pytest.mark.parametrize("adet", [0, -2])
def test_sepet_toplami_gecersiz_adet(adet):
    # 0 değeri sepet-2 hatasını yakalar
    sepet = [{"urun": "test", "fiyat": 10, "adet": adet}]
    with pytest.raises(ValueError, match="adet pozitif olmalı"):
        sepet_toplami(sepet)


# 3. en_pahali_urun testleri
@pytest.mark.parametrize("sepet, beklenen", [
    ([], None),  # pahali-2 hatasını yakalar
    ([
        {"urun": "kalem", "fiyat": 15, "adet": 5},
        {"urun": "defter", "fiyat": 45, "adet": 2},
        {"urun": "silgi", "fiyat": 10, "adet": 10}
    ], "defter"),
    ([
        {"urun": "çikolata", "fiyat": 30, "adet": 1},
        {"urun": "bisküvi", "fiyat": 30, "adet": 2},
        {"urun": "sakız", "fiyat": 5, "adet": 5}
    ], "çikolata")  # pahali-1 hatasını yakalar (aynı fiyatlı ürünlerde ilk olan)
])
def test_en_pahali_urun(sepet, beklenen):
    assert en_pahali_urun(sepet) == beklenen