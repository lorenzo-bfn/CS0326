"""
    Per la traccia degli esercizi base, esercizio n. 1, lo script chiede un numero all'utente e determina se si tratta di un numero pari o dispari
"""

if __name__ == '__main__':
    max_n_tentativi_input = 3
    n_tentativo_input_corr = 0

    while n_tentativo_input_corr <= max_n_tentativi_input:
        n = input("Inserisci un numero intero: ").strip()
        if n.isdigit(): break
        else: 
            print("AVVISO!: Non è stato inserito un numero intero. Riprovare ( Tentativi: %d/%d )" % (n_tentativo_input_corr, max_n_tentativi_input) )
            n_tentativo_input_corr = n_tentativo_input_corr + 1
            
    if n_tentativo_input_corr >= max_n_tentativi_input: exit()

    n = int(n)

    # Si fa uso dell'operatore ternario
    print( "Il numero %d è pari" % n if n % 2 == 0 else "Il numero %d è dispari" % n)

