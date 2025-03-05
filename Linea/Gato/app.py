''' Este archivo es el punto de entrada de la aplicacion '''

import tablero

def main():

 ''' Funcion principal '''

x = {"G": 0, "P": 0, "E": 0}
o = {"G": 0, "P": 0, "E": 0}
score = {"X": x, "O": o}
numeros = [str(i) for i in range(1, 10)]
corriendo = True
while corriendo:
   dsimbolos = {x: x for x in numeros}
   g = tablero.juego(dsimbolos)
   tablero.actualiza_score(score, g)
   tablero.despliega_tablero(score)
   x = input('¿Quieres jugar de nuevo? (s/n): ')

if x.lower() == 'n':
        corriendo = False
        print('¡Gracias por jugar!')

if g is not None:
         print(f'¡El ganador es {g}!')
         tablero.actualiza_score(score, g)
else:
         print('¡Empate!')
         tablero.actualiza_score(score, None)
'''
g = tablero.Tablero(dsimbolos)
if g is not None:
    print(f'¡El ganador es {g}!')
else:
    print('¡Empate!')'''


if __name__ == '__main__':
    main()
