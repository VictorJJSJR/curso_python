'''
Programa principal del juego del ahorcado
'''

import funciones as fn
import string
from random import choice

def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    Programa principal
    '''
    
    # cargamos las plantillas
    plantillas = fn.carga_plantillas('plantilla')
    # cargamos las palabras
    lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(lista_oraciones)
    o = 5 #oportunidades
    p = choice(palabras)
    abcdario = {letra:letra for letra in string.ascii_lowercase}

    
    adivinadas = set()
    while o>0:
        fn.despliega_plantilla(plantillas, o)
        o = fn.adivina_letra(abcdario, p, adivinadas, o)
        if p == ''.join([letra if letra in adivinadas else '_' for letra in p]):
            print('Ganaste')
            break
        fn.despliega_plantilla(plantillas, o)
        print(f"la palabra era: {p}")

if __name__ == '__main__':
    archivo = 'Linea/ahorcado/datos/pg15532.txt'
    main(archivo)