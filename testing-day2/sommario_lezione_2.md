# RECAP GIORNO 2: Kit di sopravvivenza, strumenti python per il testing e best practice

L'obiettivo di oggi non era imparare a programmare, ma imparare a **non spaccare i sistemi in produzione**. Di seguito trovate i comandi di sopravvivenza, i pattern architetturali e la documentazione ufficiale. Se non applicate queste regole, state scrivendo codice legacy.

## 1. Il Survival Kit (Infrastruttura e Terminale)

Il terminale è cieco, ma è un vostro alleato. Se non lo controllate, distruggerete file e inquinerete il sistema operativo.

- **`pwd` (Mac/Linux) o `Get-Location` (Windows):** Il vostro radar. Prima di fare danni, chiedetevi: _"Dove mi trovo nel sistema?"_. Non presumete mai nulla, verificate la vostra coordinata assoluta.

- **`ls` (Mac/Linux) o `dir` (Windows):** I vostri occhi. Elenca il contenuto della cartella in cui vi trovate. Usatelo prima e dopo ogni operazione per verificare che i file siano effettivamente lì

- **`cd <nome_cartella>` (Change Directory):** Il movimento. È il comando per navigare nell'albero delle directory. Per tornare indietro di un livello, usate `cd ..` e ricrodate che potete concatenare con `/` (`\` in windows)

* **Il tasto `TAB`:** Il vostro primo livello di testing. Non digitate mai i nomi interi dei file. Iniziate a scrivere e premete `TAB`. Se non si autocompleta, vi siete persi o avete fatto un `typo` (errore di battitura)

* **`mkdir <cartella>`:** Crea una cartella senza dover utilizzare interfaccia grafica

* **`touch <nome_file>` (Mac/Linux):** Creazione istantanea. Crea un file vuoto senza dover usare il noioso "Tasto destro -> Nuovo documento". Su Windows (PowerShell) l'equivalente è `New-Item <nome_file>` o l'alias `ni <nome_file>`

* **`nano <nome_file>` (Mac/Linux) o `notepad <nome_file>` (Windows):** Modifica al volo. Apre l'editor di testo direttamente dal terminale. Indispensabile quando lavorate su server remoti dove l'interfaccia grafica non esiste

* **`python -m venv venv`:** L'isolamento. Crea un "recinto" logico (Virtual Environment) per evitare l'_esplosione delle dipendenze_. Tutto ciò che fate qui dentro non rompe il resto del PC/server

* **`.\venv\Scripts\activate.psl` (Win) o `source venv/bin/activate` (Mac/Linux):** Accende il recinto. La scritta `(venv)` sul terminale è la vostra autorizzazione a procedere

* **`pip install -r requirements.txt`:** Il gestore di pacchetti `pip` è il corriere, `requirements.txt` è la lista della spesa. Garantisce che il vostro ambiente sia identico a quello dei colleghi

---

## 2. L'Arsenale: Python per il Testing

### A. Type Hinting

Python permette tutto, ma in un team questo è un incubo. Usate i _Type Hints_ per dichiarare il vostro contratto. Dicono all'IDE cosa vi aspettate, permettendogli di segnalarvi gli errori in rosso prima ancora di eseguire il codice.

```python
# In ingresso una stringa, valore di ritorno booleano
def valida_password(password: str) -> bool:
    ...
    ...
    ...

```

### B. Avoid Swallowing Errors

Molti sviluppatori "ingoiano" gli errori restituendo False o None quando qualcosa va storto (Swallowing Errors). Il programma va avanti zoppicando e corrompe i dati. Noi usiamo raise per fermare l'esecuzione istantaneamente.

```python
# valida.py

def valida_password(password: str) -> bool:
    if len(password) < 8:
        # Il Freno di Emergenza: ferma l'esecuzione all'istante
        raise ValueError("Password troppo corta")

    # Se sopravvive all'if, il codice continua
    return True

# --- ZONA DI DEMO ---
if __name__ == "__main__":
    print("--- Inizio esecuzione del sistema ---")

    # Simuliamo un input sbagliato malevolo o errato
    password_utente = "123"
    print(f"Ricevuta password dall'utente: {password_utente}")

    esito = valida_password(password_utente)

    # IL PUNTO FOCALE:
    # Se il codice non avesse il 'raise', il sistema arriverebbe qui e salverebbe l'utente con una password bucata
    # Grazie al 'raise', l'eccezione ucciderà il processo prima di questa riga
    print(f"✅ PERICOLO: Il sistema continua a girare. Esito: {esito}")
```

**Come si legge il terminale (Traceback) quando ci sono eccezioni?**
Dal basso verso l'alto. L'ultima riga (ValueError: Password troppo corta) vi dice cosa è rotto. La riga sopra vi dice il file e la linea esatta in cui dovete operare. È l'unico modo per fare debugging in produzione.

---

## 3. Primo esempio di test (con raise ed eccezioni)

Non testiamo solo quando le cose vanno bene (Happy Path). Dobbiamo testare che il nostro "freno di emergenza" funzioni quando le cose vanno male (Sad Path).

```python
# test_valida.py

import pytest
from valida import valida_password

def test_password_lunga_passa():
    """Il percorso felice (Happy Path)"""
    risultato = valida_password("PasswordSicura123!")
    assert risultato is True

def test_password_corta_lancia_errore():
    """Il test del freno di emergenza (Sad Path)"""

    # Diciamo a pytest: "So che la prossima riga esploderà. Se esplode, il test PASSA"
    with pytest.raises(ValueError, match="troppo corta"):
        valida_password("123")

```

Se un collega domani toglie il raise dalla funzione principale, questo test fallirà (diventerà rosso), impedendogli di mandare in produzione un sistema vulnerabile

---

## 4. Documentazione Ufficiale

I veri sviluppatori non copiano da chatGPT/Claude/Gemini senza capire, leggono le specifiche (RTFM - Read The Fucking Manual):

- **Comandi Base Terminale (Bash):** [Per Linux/Mac](https://ubuntu.com/tutorials/command-line-for-beginners#4-creating-folders-and-files) oppure [Per Windows (PowerShell)](https://learn.microsoft.com/en-us/powershell/scripting/learn/ps101/01-getting-started?view=powershell-7.6)

- **Documentazione Python:** docs.python.org/3.14/

- **Virtual Environments:** docs.python.org/3/library/venv.html

- **Gestione Pacchetti (PIP):** pip.pypa.io/en/stable/

- **Gestione delle Eccezioni:** docs.python.org/3/tutorial/errors.html

- **Pytest - Testare Eccezioni:** docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions
