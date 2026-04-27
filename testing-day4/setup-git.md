# SETUP INFRASTRUTTURALE: Git e Standardizzazione

Prima di iniziare a scrivere codice, l'ambiente di sviluppo deve essere configurato secondo gli standard industriali. In un team misto (Windows, Mac, Linux), l'assenza di queste configurazioni genera conflitti invisibili e distrugge la cronologia del codice.

Eseguite le istruzioni relative al vostro sistema operativo. Se il terminale vi restituisce un errore, leggete la sezione "Troubleshooting".

---

## 1. Installazione (Per Sistema Operativo)

### 🪟 WINDOWS

L'industria su Windows usa il terminale PowerShell. Dimenticate il Prompt dei comandi (`cmd`).

1. Scaricate l'installer ufficiale: [gitforwindows.org](https://gitforwindows.org/)
2. Durante l'installazione, premete sempre "Next", **ma assicuratevi che questa opzione sia spuntata:** _"Git from the command line and also from 3rd-party software"_ (Questo inietta Git nel PATH del vostro sistema).

**Troubleshooting Windows:**

- **Errore:** `git : The term 'git' is not recognized as the name of a cmdlet...`
- **Soluzione:** Git non è nel PATH o il terminale è "vecchio". Chiudete **completamente** il terminale PowerShell e riapritelo. Se il problema persiste, dovete reinstallare spuntando la casella menzionata al punto 2.

### 🍏 MACOS

Mac ha una versione di Git preinstallata da Apple, ma spesso è obsoleta e bloccata dagli strumenti di sviluppo.

1. Aprite il terminale (Launchpad -> Terminale).
2. Digitate `git --version` e premete Invio.
3. Se vi compare un pop-up che vi chiede di installare i "Command Line Developer Tools", cliccate su **Installa** e attendete.

**Troubleshooting macOS:**

- **Errore:** `xcrun: error: invalid active developer path...`
- **Soluzione:** Apple ha aggiornato il sistema operativo e ha rotto i collegamenti di Git. Per ripararlo, digitate da terminale: `xcode-select --install` e seguite la procedura a schermo.

### 🐧 LINUX (Ubuntu/Debian)

1. Aprite il terminale e digitate:
   `sudo apt update`
   `sudo apt install git -y`

**Troubleshooting Linux:**

- **Errore:** `Could not get lock /var/lib/dpkg/lock-frontend...`
- **Soluzione:** Un altro programma (come il Software Center o un aggiornamento in background) sta usando il gestore pacchetti. Chiudete i programmi di aggiornamento o aspettate due minuti e riprovate.

---

## 2. La Configurazione Architetturale (Obbligatoria per tutti)

Una volta installato, Git è stupido: non sa chi siete e non sa come gestire i file cross-platform. Aprite il terminale ed eseguite riga per riga.

### A. Identità Digitale (Niente commit anonimi)

Se non impostate questi dati, GitHub non collegherà il codice al vostro account e risulterete invisibili nel progetto. **Usate la stessa email con cui vi siete registrati su GitHub.**

```bash
git config --global user.name "Il Vostro Nome e Cognome"
git config --global user.email "la.vostra.email@esempio.com"
```

---

## 3. Autenticazione di Rete (Lo Standard Industriale)

Configurare nome ed email non vi fa "loggare" su GitHub, serve solo a firmare i vostri commit. Per permettere al terminale di inviare codice ai server di GitHub, dovete autenticarvi. Dimenticate le password: si usa il protocollo crittografico tramite la GitHub CLI

**Step 1**: Installare GitHub CLI (gh)

- **Windows:** Aprite PowerShell come Amministratore e digitate: winget install --id GitHub.cli

- **macOS:** Aprite il terminale e digitate: brew install gh (Richiede Homebrew)

- **Linux:** Aprite il terminale e digitate:
  curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null && sudo apt update && sudo apt install gh -y

**Step 2:** Il Login
Chiudete e riaprite il terminale. Digitate questo comando:

```bash
gh auth login
```

Seguite le istruzioni interattive a schermo. Quando richiesto:

1. Scegliete GitHub.com

2. Scegliete HTTPS

3. Rispondete Yes alla domanda "Authenticate Git with your GitHub credentials?"

4. Scegliete Login with a web browser

Copiate il codice a 8 cifre generato dal terminale, premete Invio per aprire il browser, incollate il codice e autorizzate.
