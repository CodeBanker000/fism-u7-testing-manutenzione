import pytest
from validatore_soluzione import valida_password

# =====================================================================
# LIVELLO 1: Il Percorso Felice (Happy Path)
# =====================================================================
def test_password_valida():
    # Se la password è perfetta, ci aspettiamo un ritorno True senza eccezioni.
    assert valida_password("ProduzioneSicura2026!") is True

# =====================================================================
# LIVELLO 2 e 3: Parametrizzazione e Intercettazione Errori
# =====================================================================
# Invece di scrivere 4 funzioni diverse, usiamo una matrice di dati.
@pytest.mark.parametrize("password_invalida, errore_atteso", [
    ("corta1A", "minimo 8 caratteri"),           # Meno di 8 caratteri
    ("tuttominuscola123", "lettera maiuscola"),  # Manca la maiuscola
    ("SENZANUMERI", "almeno un numero"),         # Manca il numero
    ("      1A", "minimo 8 caratteri")           # Edge case: spazi bianchi. Lunga 8, ma invalida logicamente se strippata (se i requisiti lo prevedessero).
])
def test_password_invalide(password_invalida, errore_atteso):
    """Verifica che ogni violazione della policy alzi l'eccezione corretta."""
    
    with pytest.raises(ValueError, match=errore_atteso):
        valida_password(password_invalida)

# =====================================================================
# LIVELLO 3: Fixtures e Gestione dell'I/O
# =====================================================================

# Leggere i file dal disco è un'operazione lenta. Se non specifichiamo lo scope,
# Pytest leggerà questo file per OGNI singolo test
# Con scope="session", il file viene letto una volta sola all'avvio della pipeline
# e tenuto in RAM (memoria) per tutti i test.
@pytest.fixture(scope="session")
def blacklist_aziendale():
    """Carica in memoria la lista delle password compromesse."""
    try:
        with open("blacklist.txt", "r") as file:
            # list per pulire i ritorni a capo (\n)
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def test_password_nella_blacklist(blacklist_aziendale):
    """Verifica che una password robusta ma compromessa venga rifiutata."""
    # Password123 rispetta i requisiti di lunghezza, numero e maiuscola, ma è nel file txt. => deve fallire
    with pytest.raises(ValueError, match="Password compromessa"):
        valida_password("Password123", blacklist=blacklist_aziendale)