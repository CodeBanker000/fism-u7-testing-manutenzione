class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0):
        self.titolare = titolare
        self.saldo = float(saldo_iniziale)

    def deposita(self, importo):
        if importo <= 0:
            raise ValueError("L'importo da depositare deve essere positivo.")
        self.saldo += importo
        return self.saldo

    def preleva(self, importo):
        """Preleva applicando una commissione di 2 euro."""
        # FIX BUG 1 (Validazione Input):
        # Se non blocco i negativi, un utente può prelevare -100 e vedersi accreditare i soldi.
        if importo <= 0:
            raise ValueError("L'importo deve essere positivo.")
            
        # FIX BUG 2 (Errore Logico Matematico):
        # La commissione è un costo aggiuntivo per l'utente, non uno sconto
        # Va sommato all'importo, non sottratto
        costo_totale = importo + 2 
        
        if costo_totale > self.saldo:
            raise ValueError("Fondi insufficienti.")
            
        self.saldo -= costo_totale
        return self.saldo

    def accredita_interessi(self, tasso):
        """Aggiunge una quota al saldo basata sul tasso."""
        # FIX BUG 3 (Precisione Floating Point):
        # 0.1 + 0.2 in Python fa 0.30000000000000004
        # Usando round() forziamo l'arrotondamento per evitare il fallimento del test di precisione
        self.saldo = round(self.saldo + tasso, 2)
        return self.saldo

    def bonifico(self, destinatario, importo):
        """Trasferisce soldi da questo conto a un altro."""
        # FIX BUG 4 (Mancanza di Rollback / Atomicità):
        # 1. Preleviamo i soldi da NOI (se l'importo è negativo, preleva lancia già un'eccezione
        #    ed esce immediatamente, lasciando il nostro saldo intatto - Test Superato)
        self.preleva(importo)
        
        # 2. Cosa succede se il conto destinatario è bloccato e deposita() fallisce?
        # Dobbiamo restituire i soldi al mittente tramite un blocco try/except
        try:
            destinatario.deposita(importo)
        except Exception as e:
            # Il destinatario ha rifiutato il deposito
            # Rollback: rimborsiamo l'importo e la commissione di 2 euro spesa per il bonifico
            self.saldo += (importo + 2)
            # Rilanciamo l'errore per avvisare il chiamante
            raise e