from typing import TypedDict

"""
    Per la traccia dello "Esercizio di Programmazione in Python: Genera un Nome per la Tua Band", lo script esegue le seguenti macro operazioni: 
        - 1. Lo script richiede all'utente di inserire su linea di comando:
            + il nome della proria città di origine.
            + il nome del prorio animale domestico
        - 2. A ricezione degli input, lo script concatena/combina il nome della città e il nome dell'animale in un'unica stringa che rappresenta il nome della band.
        - 3. Come output, lo script restituisce a schermo, ovvero nel buffer Standard Output della linea di comando, il nome generato per la band.
"""

class td_appellativi_utente(TypedDict):
    citta_origine: str
    animale_domestico: str

class banda:
    def __init__( self, appellativi_utente: td_appellativi_utente = {} ):
        
        self.nome_banda = appellativi_utente.get( 'citta_origine', input("Inserisci il nome della propria città di origine (Premi INVIO per confermare): ") )
        self.nome_banda = self.nome_banda + ' ' + appellativi_utente.get( 'animale_domestico', input("Inserisci il nome del proprio animale domestico (Premi INVIO per confermare): ") )
    
    def __str__(self):
        return "Nome della banda: %s" % self.nome_banda
        
if __name__ == '__main__':
    nuova_banda = banda()
    print( nuova_banda )