import os
import shutil
def cambiar_directorio():
    encontrado = False
    while encontrado == False:
        respuesta = input("Quieres ejecutar el programa desde \
        el directorio en el que estas? Si/No: ")
        
        if respuesta == "si" or respuesta == "Si" or respuesta == "s":
            encontrado = True
            directorio_actual = os.getcwd()
        elif respuesta == "no" or respuesta == "No" or respuesta == "n":
            directorio_actual = input("Introduce directorio \
                desde el que quieres hacer la exploracion: ")
            encontrado = True
        else:
            print("Elige una opcion valida")
    return directorio_actual

def separa_nombre_archivo(directorio):
    separados = directorio.split("\\")
    nombre_archivo = separados.pop()
    """strin = ""
    for dire in separados:
        strin = strin + dire + "\\"
    strin = strin[0:len(strin) - 1]
    """
    return nombre_archivo

def intentar_leer_archivo(directorio):
    try:
        archivo = open(directorio,"r")
        archivo.close()
        return True
    except:
        return False


def recorre_archivos(directorio_actual,destino):
    lista_directorios = os.listdir(directorio_actual)
    for directorio_files in lista_directorios:
        directorio_files_def = directorio_actual + "\\" + directorio_files
        if os.path.isfile(directorio_files_def):
            if intentar_leer_archivo(directorio_files_def): #si consigue leer el archivo
                #copiamos el archivo en la ruta de destino
                nombre = separa_nombre_archivo(directorio_files_def)
                destino2 = destino +"\\" + nombre
                print("directorio1 = ", directorio_files_def)
                print("destino = ", destino2)
                shutil.copy(directorio_files_def, destino2)
            
        else:
            destino = destino + "\\" + directorio_files 
            os.mkdir(destino)
            recorre_archivos(directorio_files_def,destino)
    

directorio_actual = os.getcwd()
print("Este es tu directorio actual: " + directorio_actual)
directorio_actual = cambiar_directorio()
destino = input("Donde quieres que se copien los archivos?: ")
recorre_archivos(directorio_actual,destino)



