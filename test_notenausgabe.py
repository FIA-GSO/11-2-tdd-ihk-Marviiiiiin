import pytest
from notenausgabe import *

def test_notenausgabe__negativ_prozentwert():
    with pytest.raises(ValueError):
        notenausgabe(-1)

def test_notenausgabe__ueber_prozentwert():
    with pytest.raises(ValueError):
        notenausgabe(101)

def test_notenausgabe_falscher_datentyp():
    with pytest.raises(TypeError):
        notenausgabe("test")

def test_notenausgabe_keine_punkte():
    assert notenausgabe(0) == "ungenügend"

def test_notenausgabe_noch_ungenugend():
    assert notenausgabe(29) == "ungenügend"

def test_notenausgabe_gerade_mangelhaft():
    assert notenausgabe(30) == "mangelhaft"

def test_notenausgabe_noch_mangelhaft():
    assert notenausgabe(49) == "mangelhaft"

def test_notenausgabe_gerade_ausreichend():
    assert notenausgabe(50) == "ausreichend"

def test_notenausgabe_noch_ausreichend():
    assert notenausgabe(66) == "ausreichend"

def test_notenausgabe_gerade_befriedigend():
    assert notenausgabe(67) == "befriedigend"

def test_notenausgabe_noch_befriedigend():
    assert notenausgabe(80) == "befriedigend"

def test_notenausgabe_gerade_gut():
    assert notenausgabe(81) == "gut"

def test_notenausgabe_noch_gut():
    assert notenausgabe(91) == "gut"

def test_notenausgabe_gerade_sehr_gut():
    assert notenausgabe(92) == "sehr gut"

def test_notenausgabe_maximal_punkte():
    assert notenausgabe(100) == "sehr gut"