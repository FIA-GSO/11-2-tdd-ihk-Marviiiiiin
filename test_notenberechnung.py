from notenberechnung import *
import pytest

def test_notenberechnung__maximal_punkte():
    assert notenberechnung(100, 100) == 100.0

def test_notenberechnung__haelfte_punkte():
    assert notenberechnung(50, 100) == 50.0

def test_notenberechnung__niedrigste_punkte():
    assert notenberechnung(0, 100) == 0.0

def test_notenberechnung__negative_punkte():
    with pytest.raises(ValueError):
        notenberechnung(-1, 100)

def test_notenberechnung__unter_mindest_gesamtpunkte_zur_notenberechnung():
    with pytest.raises(ValueError):
        notenberechnung(0, 5)

def test_notenberechnung__mindest_gesamtpunktzahl():
    assert notenberechnung(0, 6) == 0.0

def test_notenberechnung__falscher_datentyp_punkte():
    with pytest.raises(TypeError):
        notenberechnung("test", 100)

def test_notenberechnung__falscher_datentyp_gesamitpunkte():
    with pytest.raises(TypeError):
        notenberechnung(100, "test")

def test_notenberechnung__ueberschreitung_der_gesamtpunkte():
    with pytest.raises(ValueError):
        notenberechnung(101, 100)


