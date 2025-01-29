'''
tablero.py: Dibuja el tablero del juego del gato.
'''

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

if __name__ == '__main__':
    # Crear el diccionario con claves tipo string
    simbolos = {str(x): str(x) for x in range(1, 10)}
    
    dibujar_tablero(simbolos)

    # Modificar el diccionario correctamente
    simbolos['1'] = 'X'
    dibujar_tablero(simbolos)

    simbolos['5'] = 'O'
    dibujar_tablero(simbolos)
