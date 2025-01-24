#Calculo de y en funcion de x
from funciones import calcular_y

def main():  
    m = 2
    b = 3
    x = 5
    y = calcular_y(x, m, b) 
    print(f'Para x= {x}, Para y= {y}') 

if __name__ == "__main__": 
    main()