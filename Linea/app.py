''' cálculo de coordenadas de líneas '''
import argparse
import matplotlib.pyplot as plt
import funciones


def main(m:float, b:float):
    X = [x/10.0 for x in range(10,110,5)]
    Y = [funciones.calcular_y(x, m, b) for x in X]
    coordenadas_flotantes = list(zip(X,Y))
    print("Flotantes:")
    print(coordenadas_flotantes)
    plt.plot(X,Y)
    plt.title(f'Linea con pendiente {m} y ordenada al origen {b}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', type=float, help='Pendiente de la línea', default=2.0)
    parser.add_argument('-b', type=float, help='Ordenada al origen')
    args = parser.parse_args()
    main(args.m, args.b)
    #main(m=2.0, b=3.0)