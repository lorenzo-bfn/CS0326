# Author: lorenzo-bfn

from decimal import Decimal
from typing import Literal
import re, math

def inputNumero( msg_prompt = None, max_n = None, msg_errore = None , è_decimale = False ):
    max_n_tentativi_input = 3
    n_tentativo_input_corr = 1

    while n_tentativo_input_corr <= max_n_tentativi_input:
        n = input("%s: " % msg_prompt ).strip()
        if è_decimale :
            if re.match('(?:\s*\d*(?:\.|,)\d*\s*|\s*\d*\s*)', n):
                if max_n:
                    n = Decimal(n)
                    if n <= max_n: break
                    elif msg_errore:
                        print(msg_errore)
                        n_tentativo_input_corr = n_tentativo_input_corr + 1
                else:
                    break
            else: 
                print("AVVISO!: Non è stato inserito un numero decimale. Riprovare ( Tentativi: %d/%d )" % (n_tentativo_input_corr, max_n_tentativi_input) )
                n_tentativo_input_corr = n_tentativo_input_corr + 1    
        else:
            if n.isdigit():
                if max_n:
                    n = int(n)
                    if n <= max_n: break
                    elif msg_errore:
                        print( "%s ( Tentativi: %d/%d )" % (msg_errore,n_tentativo_input_corr, max_n_tentativi_input) )
                        n_tentativo_input_corr = n_tentativo_input_corr + 1
                else:
                    break
            else: 
                print("AVVISO!: Non è stato inserito un numero intero. Riprovare ( Tentativi: %d/%d )" % (n_tentativo_input_corr, max_n_tentativi_input) )
                n_tentativo_input_corr = n_tentativo_input_corr + 1
    
    if n_tentativo_input_corr >= max_n_tentativi_input: exit()
    
    if è_decimale: n = Decimal(n.replace(',','.'))
    else: n = int( n )
    
    return n

def ottieniPerimetro(tipo_figura : Literal["QUADRATO","CERCHIO","RETTANGOLO"] = None, **kwargs ):
    """
    **fun. ottientPerimetro**
    
    Argomenti:
      - `tipo_figura` (str): Tipo della figura geometrica. E' previsto che il valore sia una delle seguenti stringhe:
            + `"QUADRATO"`
            + `"CERCHIO"`
            + `"RETTANGOLO"`
      - `lato` (Decimal): Letto dalla funzione se `tipo_figura` è `QUADRATO`. Lunghezza del lato della figura geometrica;
      - `r` o `raggio` (Decimal): Letto dalla funzione se `tipo_figura` è `CERCHIO`. Raggio del cerchio geometrico;
      - `base` (Decimal): Letto dalla funzione se `tipo_figura` è `RETTANGOLO`. Lunghezza della base della figura geometrica;
      - `alteza` (Decimal): Letto dalla funzione se `tipo_figura` è `RETTANGOLO`. Lunghezza della altezza della figura geometrica;
    """
    if tipo_figura == "QUADRATO":
        lato = kwargs.get("lato", inputNumero( msg_prompt="Inserisci la lunghezza del lato del quadrato", è_decimale=True))
        if lato: return lato * 4
    
    elif tipo_figura == "CERCHIO":
        r = kwargs.get("r", kwargs.get("raggio", inputNumero( msg_prompt="Inserisci il raggio della circonferenza", è_decimale=True)) )
        if r: return ( 2 * Decimal.from_float(math.pi) * r )
        
    elif tipo_figura == "RETTANGOLO":
        base = kwargs.get("base", inputNumero( msg_prompt="Inserisci la lunghezza della base del rettangolo", è_decimale=True) )
        altezza = kwargs.get("altezza", inputNumero( msg_prompt="Inserisci la lunghezza della altezza del rettangolo", è_decimale=True) )
        if base and altezza: return ( ( base * 2 ) + ( altezza * 2 ) )
        
if __name__ == '__main__':
    print("Calcolo perimetro: Seleziona il numero del tipo della figura:")
    print("    1 -> Quadrato")
    print("    2 -> Cerchio")
    print("    3 -> Rettangolo")
    tipi_figure = ["QUADRATO","CERCHIO","RETTANGOLO"]
    
    p = inputNumero(
        msg_prompt = "Inserisci un numero intero",
        max_n = tipi_figure.__len__(),
        msg_errore = "AVVISO!: L'indice non corrisponde alle opzioni disponibili. Riprovare"
    )
    
    perimetro = ottieniPerimetro( tipi_figure[ p-1 ] )
    print("La circonferenza del %s è %.3f UdM" % (tipi_figure[ p-1 ], perimetro) if (p-1) == 1 else "Il perimetro del %s è %.3f UdM" % (tipi_figure[ p-1 ], perimetro) )