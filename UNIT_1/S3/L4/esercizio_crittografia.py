# Author: lorenzo-bfn

import base64, argparse, sys, math

def encryptCaesarROT13(message, key, alphabet):
    ciphertext = ""
    for old_character in message:
        new_character = ""
        if(old_character in alphabet):
            index = alphabet.index(old_character)
            new_index = (index + key) % len(alphabet)
            new_character = alphabet[new_index]
        ciphertext = ciphertext + new_character
    return ciphertext

def decryptCaesarROT13(message, key, alphabet):
    if isinstance( key, str):
        key = key.strip()
        if key.isdigit(): key = int( key )
    plaintext = encryptCaesarROT13(message, 0 - key, alphabet)
    return plaintext

def shift_letters(text, shift):
    result = []
    
    for char in text:
        if char.isupper():
            shifted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted_char)
        elif char.islower():
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted_char)
        else:
            result.append(char)
            
    return "".join(result)



stringa_crittografata_1 =  "HSNFRGH"
chiave = '27'
alfabeto = 'ABCDEFGHILMNOPQRSTUVWXYZ'

stringa_decrittata_1 = decryptCaesarROT13( stringa_crittografata_1, chiave, alfabeto)

print( "== Stringa crittografata %s ===\n -> Stringa decrittata: %s \sMetodo: Caesar / ROT13 - Chiave %s - Alfabeto utilizzato: %s\n" % (
    stringa_crittografata_1, stringa_decrittata_1, chiave, alfabeto
) )

stringa_crittografata_2 = "QWJhIHZ6b2VidHl2bmdyIHB1ciB6ciBhciBucHBiZXRi"
print( "== Stringa crittografata %s ===\n" % stringa_crittografata_2 )
stringa_decrittata_2_base64 = base64.b64decode(stringa_crittografata_2).decode('utf-8')

print( " -> Step intermedio: stringa decrittata con algoritmo Base64: %s " % stringa_decrittata_2_base64 )
print( " -> Traslazione del codice ASCII dei caratteri in ciclo iterativo da valore 0 a valore 20: %s " % stringa_decrittata_2_base64 )
for i in range(0,20):
    stringa_decrittata_traslata = shift_letters(stringa_decrittata_2_base64, i)
    print(f" - Stringa traslata di {i}: {stringa_decrittata_traslata}")
print(" -> La stringa con testo comprensibile da un essere umano è quella traslata da un valore pari a 13.")
print(" -> Stringa decrittata: %s" % shift_letters(stringa_decrittata_2_base64, 13))