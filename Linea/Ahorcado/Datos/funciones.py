'''
Maneja las funciones necesarias para el funcionamiento basico del programa
'''

def cargar_archivo_texto(archivo: str) -> list:
    '''
    Carga un archivo de texto y devuelve una lista con las oraciones del archivo
    '''
    with open(archivo, 'r', encoding='utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantillas: str) -> dict:
    '''
    Carga las plantillas de los archivos de texto y las guarda en un diccionario
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = cargar_archivo_texto(f"./Plantillas/{nombre_plantillas}-{i}.txt")
    return plantillas

if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    print(plantilla[0])  
