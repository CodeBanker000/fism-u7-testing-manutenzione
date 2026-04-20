import datetime
from unittest.mock import patch

"""
#"nome_modulo.libreria_importata.funzione"
@patch('prova.random.randint)
def test_vittoria(mock_randint):
    #setup
    mock_randint.return_value = 6
    #esecuzione
    risultato = lancia_dado_magico()

    #verifica
    assert risultato
"""

def licenza_scaduta(data_scadenza: str) -> bool:
    """Ritorna True se la licenza è scaduta rispetto a OGGI.
    Formato data: 'YYYY-MM-DD'
    """
    scadenza = datetime.datetime.strptime(data_scadenza, "%Y-%m-%d")
    oggi = datetime.datetime.now()
    
    return oggi > scadenza