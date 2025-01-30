'''
tablero.py: Dibuja el tablero del juego del gato.
'''
import random

def dibujar_tablero(simbolos: dict):
    '''
    Dibuja el tablero del juego del gato.
    '''
    print(f'''
    
    {simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    ---------
    {simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    ---------
    {simbolos['7']} | {simbolos['8']} | {simbolos['9']}
    ''')

def ia(simbolos: dict):
    '''Juega Maquina'''
    ocupado = True
    while ocupado == True:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos: dict):
    '''Juega usuario'''
    lista_numeros = [str(i) for i in range(1, 10)]
    ocupado = True
    while ocupado == True:
     x = input('Ingresa el numero de la casilla: ')
    if x in lista_numeros:
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'X'
            ocupado = False
        else:
            print('Casilla ocupada')
    else:
        print('Numero no valido')


if __name__ == '__main__':
    # Crear el diccionario con claves tipo string
    numeros = [ str(i) for i in range(1, 10)]
    simbolos = {str(x): str(x) for x in range(1, 10)}
    
    dibujar_tablero(simbolos)
    ia(simbolos)
    #x = random.choice(numeros)
    #numeros.remove(x)
    #simbolos[x] = 'X'
    dibujar_tablero(simbolos)
    usuario(simbolos)
    #o = random.choice(numeros)
    #numeros.remove(o)
    #simbolos[o] = 'O'
    dibujar_tablero(simbolos)
    #print(numeros)
    # Modificar el diccionario correctamente
    #simbolos['1'] = 'X'
    #dibujar_tablero(simbolos)

    #simbolos['5'] = 'O'
    #dibujar_tablero(simbolos)
