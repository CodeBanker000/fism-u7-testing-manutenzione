import sys

def main():
    if len(sys.argv) < 2:
        # Scriviamo su stderr per indicare un problema
        sys.stderr.write("ERRORE CRITICO: Devi fornire un nome utente.\n")
        sys.exit(1) # Il programma muore comunicando Errore 1 al Sistema Operativo
    
    nome_utente = sys.argv[1]

    if nome_utente.lower() == "admin" or nome_utente.lower() == "root":
        sys.stderr.write("VIOLAZIONE: L'utente 'admin'/'root' è riservato.\n")
        sys.exit(2)
        
    # Scriviamo su stdout (il print standard)
    print(f"[{nome_utente.upper()}] - Token di accesso generato: 987654321")
    sys.exit(0)

if __name__ == "__main__":
    main()