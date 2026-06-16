"""
    Per la traccia degli esercizi base, esercizio n. 6, lo script chiede all'utente una stringa e ne ritorna la stessa ma invertita
"""

if __name__ == '__main__':

    
    print("Inserisci il testo di una stringa: ")
    stringa = input()

    stringa_inv = ''
    i = stringa.__len__() - 1
    while i >= 0: 
        stringa_inv = stringa_inv + stringa[i]
        i = i - 1
    print( "La stringa inserita, ma invertita:")
    print( stringa_inv )

