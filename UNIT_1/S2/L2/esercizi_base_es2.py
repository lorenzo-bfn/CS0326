"""
    Per la traccia degli esercizi base, esercizio n. 2, lo script chiede tre numeri all'utente e ne ritorna la media
"""

if __name__ == '__main__':
    
    numeri = []
    for i in range(0, 3):
        max_n_tentativi_input = 3
        n_tentativo_input_corr = 0

        while n_tentativo_input_corr <= max_n_tentativi_input:
            n = input("Inserisci un numero intero per la media (Numeri inseriti %d/3): " % numeri.__len__() ).strip()
            if n.isdigit(): break
            else: 
                print("AVVISO!: Non è stato inserito un numero intero. Riprovare ( Tentativi: %d/%d )" % (n_tentativo_input_corr, max_n_tentativi_input) )
                n_tentativo_input_corr = n_tentativo_input_corr + 1
                
        if n_tentativo_input_corr >= max_n_tentativi_input: exit()

        numeri.append( int(n) )

    # Si fa uso della funzione sum
    print( "La media dei numeri %s è %d" % ( ', '.join( [ '%d' % _ for _ in numeri] ), ( sum( numeri ) / numeri.__len__() ) ) )

