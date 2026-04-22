import pytest
from pagamenti import elabora_pagamento

# =====================================================================
# LIVELLO 1: Test base delle eccezioni (Senza Mock)
# =====================================================================

def test_importo_negativo_lancia_errore():
    with pytest.raises(ValueError, match="maggiore di zero"):
        elabora_pagamento("carta", 100.0, -10.0)

def test_metodo_non_supportato_lancia_errore():
    with pytest.raises(ValueError, match="non supportato"):
        elabora_pagamento("contanti", 100.0, 50.0)

def test_fondi_insufficienti_lancia_errore():
    with pytest.raises(ValueError, match="Fondi insufficienti"):
        elabora_pagamento("paypal", 10.0, 50.0)