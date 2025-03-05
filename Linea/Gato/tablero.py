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
    while ocupado:
        x = random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X','O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos: dict):
    '''Juega usuario'''
    lista_numeros = [str(i) for i in range(1, 10)]
    ocupado = True
    while ocupado:
        x = input('Ingresa el numero de la casilla: ')
        if x in lista_numeros:
            if simbolos[x] not in ['X','O']:
                simbolos[x] = 'X'
                ocupado = False
            else:
                print('Casilla ocupada')
        else:
            print('Numero no valido')

def condiciones_winner(simbolos: dict):
    '''Verifica si hay un ganador'''
    combinaciones = [
        ('1', '2', '3'), ('4', '5', '6'), ('7', '8', '9'), # Filas
        ('1', '4', '7'), ('2', '5', '8'), ('3', '6', '9'), # Columnas
        ('1', '5', '9'), ('3', '5', '7') # Diagonales
    ]
    
    for c in combinaciones:
        if simbolos[c[0]] == simbolos[c[1]] == simbolos[c[2]]:
            return simbolos[c[0]] # Devuelve 'X' o 'O' si hay ganador
    
    return None

def actualiza_score(score: dict, ganador: str):
    '''Actualiza el score'''
    x = score["X"]
    o = score["O"]
    if ganador is not None:
        print(f'¡El ganador es {ganador}!')
        if ganador == 'X':
            x["G"] += 1
            o["P"] += 1
        elif ganador == 'O':
            o["G"] += 1
            x["P"] += 1

    else:
        print('¡Es un empate!')
        x["E"] += 1
        o["E"] += 1


def despliega_tablero(score:dict):
    '''Despliega el tablero'''	
    print(f'''
          X | G: {score["X"]["G"]} | P: {score["X"]["P"]} | E: {score["X"]["E"]}
            O | G: {score["O"]["G"]} | P: {score["O"]["P"]} | E: {score["O"]["E"]}
    ''')


if __name__ == '__main__':
    simbolos = {str(x): str(x) for x in range(1, 10)}
    ganador = None
    turnos = 0
    
    while not ganador and turnos < 9:
        dibujar_tablero(simbolos)
        usuario(simbolos)
        turnos += 1
        ganador = condiciones_winner(simbolos)
        if ganador or turnos == 9:
            break
        ia(simbolos)
        turnos += 1
        ganador = condiciones_winner(simbolos)
    
    dibujar_tablero(simbolos)
    if ganador:
        print(f'¡El ganador es {ganador}!')
    else:
        print('¡Es un empate!')
