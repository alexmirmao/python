"""
@author: alexmirmao
@mail: alexmirmao@gmail.com
"""
import os
def recorre_archivos(directorio_actual):
    """
    Funcion que recorre todos los directorios y subdirectorios dentro del 
    path actual en busqueda de archivos en esas carpetas y subcarpetas.

    """
    #imprime tanto los archivos como los directorios en el primer nivel del directorio actual
    lista_directorios = os.listdir(directorio_actual)
    #lista directorios guarda todos los archivos y 
    #directorios de primer nivel del directorio en el 
    # que nos encontramos
    for directorio_files in lista_directorios:
        directorio_files = directorio_actual + "\\" + directorio_files
        if os.path.isfile(directorio_files):
            print("archivo: " + directorio_files)
            
        else:
            
            recorre_archivos(directorio_files)

