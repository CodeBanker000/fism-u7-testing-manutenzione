from unittest.mock import patch
from pagamenti import elabora_pagamento

# Intercettiamo ESATTAMENTE dove la funzione viene usata (nel file pagamenti)
@patch('pagamenti.autorizza_transazione')
def test_pagamento_rifiutato_dalla_banca(mock_autorizza):
    # Diciamo al mock di rispondere sempre False
    mock_autorizza.return_value = False
    
    # Eseguiamo con dati validi
    risultato = elabora_pagamento("carta", 500.0, 50.0)
    assert risultato == "Transazione rifiutata dalla banca."

@patch('pagamenti.autorizza_transazione')
def test_pagamento_completato_con_successo(mock_autorizza):
    # Diciamo al mock di rispondere sempre True
    mock_autorizza.return_value = True
    
    risultato = elabora_pagamento("carta", 500.0, 50.0)
    assert risultato == "Pagamento completato con successo."