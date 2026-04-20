def valida_password(password: str, blacklist: list = None) -> bool:
    """
    Verifica che la password rispetti le policy di sicurezza aziendali.
    """
    # 1. Controllo base: Lunghezza
    if len(password) < 8:
        raise ValueError("Password troppo corta (minimo 8 caratteri)")
    
    # 2. Controllo complessità: Numeri
    if not any(char.isdigit() for char in password):
        raise ValueError("La password deve contenere almeno un numero")
        
    # 3. Controllo complessità: Maiuscole
    if not any(char.isupper() for char in password):
        raise ValueError("La password deve contenere almeno una lettera maiuscola")
        
    # 4. Livello 3: Controllo contro dizionario di password compromesse
    if blacklist and password in blacklist:
        raise ValueError("Password compromessa trovata nella blacklist")
        
    return True