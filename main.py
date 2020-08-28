import os
import json
import re

arreglo = []

def main():
    salir = False
    
    while not salir:
        tmpentrada = input(">>")
        entrada = tmpentrada.split(" ")

        if entrada[0].lower() == ("cargar").lower():
            readfil(tmpentrada)
        elif entrada[0].lower() ==("seleccionar").lower():
            seleccion(tmpentrada)
        elif entrada[0].lower() ==("maximo").lower():
            print("sptm es el max")
        elif entrada[0].lower() ==("minimo").lower():
            print("sptm es el min")
        elif entrada[0].lower() ==("suma").lower():
            print("sptm esta sumando")
        elif entrada[0].lower() ==("cuenta").lower():
            print("sptm esta contando")
        elif entrada[0].lower() ==("reportar").lower():
            print("sptm esta reportando")
        elif entrada[0].lower() ==("salir").lower():
            salir = True

#funcion para abrir archivos
#agregar los elementos al arreglo
def readfil(archivos):
    x = archivos.replace(",", " ")          
    listFiles = x.split(" ")
    listFiles.pop(0)

    for file in listFiles:     
        print(file)
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, str(file))
        print(path)
        with open (path) as data: 
            tmpFile = json.loads(data.read())   
            for newData in tmpFile:              
                arreglo.append(newData)           
                print(arreglo)

#SELECCIONAR nombre, edad, promedio, activo DONDE nombre = “Francisco”
#SELECCIONAR * Donde
#SELECCIONAR nombre, edad DONDE promedio = 14.45

def seleccion(cadena):
    #guardar en arreglo datos 
    y = cadena.replace(",", "")          
    list_atrib = y.split(" ")
    list_atrib.pop(0)
    print(list_atrib)
    #tmp_cond = re.findall("Donde",cadena, re.IGNORECASE)

    if list_atrib[0] == "*":
        print("seleccione todos los atributos")
        buscarCondicion(cadena)
    else:
        print("no pues toma los atributos")
        buscarCondicion(cadena)
        

    #if condicion == True:

def buscarCondicion(cadenaentrante):
    print("me salio esto --> " + cadenaentrante)
    if re.search(r"^donde.nombre$", cadenaentrante):
        print("encuentra el nombre | busca por nombre")
    elif re.search(r"^donde.promedio$", cadenaentrante):
        print("busca por promedio el prro")
        
   

#for libro in lista:
 #           print("Libro No.: " + str(cont))
  #          print("Titulo de libro : " + libro.get("nombre"))
   #         print("Autor : "+ libro.get("autor"))
    #        print("Genero : "+ libro.get("genero"))
     #       print("Fecha de Publicacion: " + str(libro.get("fecha")))




main()
