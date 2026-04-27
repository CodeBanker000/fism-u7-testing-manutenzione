import pytest
from unittest.mock import patch
from contextlib import nullcontext as does_not_raise
from pagamenti import elabora_pagamento, autorizza_transazione

# =====================================================================
# LIVELLO 3: Soluzione Universale (100% Branch Coverage)
# =====================================================================

# Applichiamo il mock a tutto il test. Se il codice si ferma prima (es. ValueError), 
# il mock semplicemente non verrà usato. Nessun problema.
@patch('pagamenti.autorizza_transazione')
@pytest.mark.parametrize("metodo, saldo, importo, esito_banca, aspettativa, output_atteso", [
    
    # --- PERCORSI DI ERRORE (Il mock viene ignorato) ---
    ("carta", 100, 0,   None, pytest.raises(ValueError, match="maggiore di zero"), None),
    ("cash",  100, 50,  None, pytest.raises(ValueError, match="non supportato"), None),
    ("crypto", 500, 50, None, pytest.raises(ValueError, match="minimo per le crypto"), None), # Testa la prima metà dell'AND
    ("carta", 10,  50,  None, pytest.raises(ValueError, match="Fondi insufficienti"), None),
    
    # --- PERCORSI VALIDI (Il mock entra in azione) ---
    # Banca rifiuta (False)
    ("carta", 500, 50,  False, does_not_raise(), "Transazione rifiutata dalla banca."),
    # Banca accetta (True) - Pagamento standard
    ("crypto", 500, 150, True, does_not_raise(), "Pagamento completato con successo."), # Testa l'altra metà dell'AND
    # Banca accetta (True) - Controllo anti-riciclaggio (>1000)
    ("paypal", 5000, 1500, True, does_not_raise(), "Pagamento completato. Richiesta verifica anti-riciclaggio.")
])
def test_pagamento_universale(mock_auth, metodo, saldo, importo, esito_banca, aspettativa, output_atteso):
    """
    Un test per dominarli tutti. Mappa ogni singolo branch logico del codice.
    """
    # Configuriamo il mock in base a cosa ci dice la matrice dati
    mock_auth.return_value = esito_banca
    
    with aspettativa:
        risultato = elabora_pagamento(metodo, saldo, importo)
        assert risultato == output_atteso

@patch('pagamenti.random.choice')
def test_autorizza_transazione(mock_choice):
    """Testa la funzione di autorizzazione isolando la dipendenza randomica."""
    # Simuliamo che random.choice restituisca True
    mock_choice.return_value = True
    
    esito = autorizza_transazione(150.0)
    
    # Verifichiamo il comportamento e che il metodo interno sia stato chiamato correttamente
    assert esito is True
    mock_choice.assert_called_once_with([True, False])        