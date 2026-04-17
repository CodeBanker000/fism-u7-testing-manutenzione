from spedizioni import calcola_spedizione
import pytest
from contextlib import nullcontext as does_not_raise

def test_spedizione_eu_leggera():
    assert calcola_spedizione(1.5, "EU") == 5.0

def test_spedizione_eu_pesante():
    assert calcola_spedizione(3.0, "EU") == 10.0

def test_spedizione_usa_leggera():
    assert calcola_spedizione(1.5, "USA") == 15.0

def test_spedizione_usa_pesante():
    assert calcola_spedizione(5.0, "USA") == 25.0

def test_peso_invalido():
    with pytest.raises(ValueError, match="positivo"):
        calcola_spedizione(-1.0, "EU")

""" @pytest.mark.parametrize("peso, zona, expected, match_msg", [
    (1.5, "EU", 5.0, None),
    (3, "EU", 10.0, None),
    (1.5, "USA", 15.0, None),
    (5.0, "USA", 25.0, None),
    (-1.0, "EU", ValueError, "Il peso deve essere positivo")
])

def test_spedizione_parametrizzato(peso, zona, expected, match_msg):
    #if type(expected) == type and issubclass(expected, Exception):
    if expected is None:
        with pytest.raises(expected, match=match_msg):
            calcola_spedizione(peso, zona)
    else:
        assert calcola_spedizione(peso, zona) == expected """

@pytest.mark.parametrize("peso, zona, expected, risultato", [
    # Happy path
    (1.5, "EU", does_not_raise(), 5.0),
    (3.0, "EU", does_not_raise(), 10.0),
    (1.5, "USA", does_not_raise(), 15.0),
    (5.0, "USA", does_not_raise(), 25.0),
    # Exceptions
    (-1.0, "EU", pytest.raises(ValueError, match="Il peso deve essere positivo"), None),
    (1.0, "AUS", pytest.raises(ValueError, match="Zona non supportata"), None)
])

def test_spedizione_parametrizzato(peso, zona, expected, risultato):
    with expected:
        assert calcola_spedizione(peso, zona) == risultato