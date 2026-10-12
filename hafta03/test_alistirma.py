import pytest

from alistirma import kargo_ucreti, bilet_fiyati, ortalama


@pytest.mark.parametrize("tutar, beklenen", [
    (0, 50),
    (250, 50),
    (499.99, 50),
    (500, 0),
    (800, 0),
])
def test_kargo_ucreti(tutar, beklenen):
    assert kargo_ucreti(tutar) == beklenen


def test_kargo_negatif_tutar():
    with pytest.raises(ValueError):
        kargo_ucreti(-1)


@pytest.mark.parametrize("yas, beklenen", [
    (0, 0),
    (6, 0),
    (7, 50),
    (17, 50),
    (18, 100),
    (64, 100),
    (65, 60),
    (80, 60),
])
def test_bilet_fiyati(yas, beklenen):
    assert bilet_fiyati(yas) == beklenen


def test_bilet_negatif_yas():
    with pytest.raises(ValueError):
        bilet_fiyati(-1)


@pytest.mark.parametrize("notlar, beklenen", [
    ([70, 85], 77.5),
    ([60, 80, 100], 80),
    ([75], 75),
])
def test_ortalama(notlar, beklenen):
    assert ortalama(notlar) == pytest.approx(beklenen)


def test_ortalama_bos_liste():
    with pytest.raises(ValueError):
        ortalama([])