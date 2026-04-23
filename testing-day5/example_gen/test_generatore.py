# MAI IMPORTARE I MODULI/FUNZIONI CHE VOGLIAMO TESTARE
import pytest
import subprocess

def test_generatore(argomenti: list[str]):
    comando_base = ["python", "generatore.py"]
    comando_completo =comando_base + argomenti

    risultato = subprocess.run(comando_completo, capture_output=True, text=True)
    return risultato



def test_nessun_parametro_ritorna_exit_code_1():
    risultato = test_generatore([])
    
    # 1. Il contratto di sistema: Esigo che fallisca con codice 1
    assert risultato.returncode == 1, f"Exit code errato: {risultato.returncode}"
    
    # 2. Il contratto testuale: L'errore deve essere sullo standard error, non sull'output
    assert "Devi fornire un nome utente" in risultato.stderr
    assert risultato.stdout == "" # Lo standard output deve essere immacolato

def test_utente_admin_ritorna_exit_code_2():
    risultato = test_generatore(["admin"])
    
    assert risultato.returncode == 2
    assert "riservato" in risultato.stderr
    assert risultato.stdout == ""

def test_utente_valido_ritorna_exit_code_0():
    risultato = test_generatore(["giovanni"])
    
    assert risultato.returncode == 0
    # Questa volta il testo atteso è su stdout, perché è un successo
    assert "Token di accesso generato" in risultato.stdout
    assert "GIOVANNI" in risultato.stdout
    assert risultato.stderr == ""