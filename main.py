import os
import json
import re
import webbrowser
import report

allatrib = ['nombre',"edad",'activo','promedio']
arreglo = []

def main():
    salir = False  
    while not salir:
        print()
        tmpentrada = input("Practica_LFP>")
        entrada = tmpentrada.split(" ")

        if entrada[0].lower() == ("cargar").lower():
            readfil(tmpentrada)
        elif entrada[0].lower() ==("seleccionar").lower():
            seleccion(tmpentrada)
        elif entrada[0].lower() ==("maximo").lower():
            maximo(entrada[1])
        elif entrada[0].lower() ==("minimo").lower():
            minimo(entrada[1])
        elif entrada[0].lower() ==("suma").lower():
            suma(entrada[1])
        elif entrada[0].lower() ==("cuenta").lower():
            print("La cantidad de regisros agregaso hasta ahora es de : " + str(len(arreglo)))
        elif entrada[0].lower() ==("reportar").lower():
            reporte(entrada[1])
        elif entrada[0].lower() ==("salir").lower():
            salir = True

def readfil(archivos):
    x = archivos.replace(",", "")          
    listFiles = x.split(" ")
    listFiles.pop(0)
    for file in listFiles:     
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, str(file))
        with open (path) as data: 
            tmpFile = json.loads(data.read())   
            for newData in tmpFile:              
                arreglo.append(newData)
    print("Archivos cargados con exito\n")

def seleccion(cadena):
    #guardar en arreglo datos 
    y = cadena.replace(",", "")  
    z = y.replace("\"", "")        
    list_atrib = z.split(" ")
    list_atrib.pop(0)
    latrib = list_atrib[:]
    print()
    if list_atrib[0] == "*":
        match = re.search("donde",cadena,re.IGNORECASE)
        if match:
           buscarCondicion(allatrib,list_atrib[-1],list_atrib[-3])
        else:
            for data in arreglo:  
                for atributo in allatrib:                                      
                    print(atributo + ":  " + str(data.get(atributo)))
                print("-------------------------------------------\n")
    else:
        for i in range(4):
            latrib.pop(-1)
        buscarCondicion(latrib,list_atrib[-1],list_atrib[-3])

def buscarCondicion(lista_atributos, atrib_buscar, name_atrib):
    for data in arreglo:                                        
        if str(atrib_buscar) == str(data.get(name_atrib)):
            for atributo in lista_atributos:
                print(atributo + ":  " + str(data.get(atributo)))
            print("-------------------------------------------\n")

def maximo(buscar_max):
    print()
    if buscar_max == "edad":
            tmp = max(arreglo, key=lambda x:x["edad"])
            
            print(tmp.get("nombre"))
            print(tmp.get("edad"))
            print("----------------------------------")
    else:
            tmp2 = max(arreglo, key=lambda x:x["promedio"]) 
            print(tmp2.get("nombre"))
            print(tmp2.get("promedio"))
            print("----------------------------------")

def minimo(buscar_min):
    print()
    if buscar_min == "edad":
            tmp = min(arreglo, key=lambda x:x["edad"])
            print(tmp.get("nombre"))
            print(tmp.get("edad"))
            print("----------------------------------")
    else:
            tmp2 = min(arreglo, key=lambda x:x["promedio"]) 
            print(tmp2.get("nombre"))
            print(tmp2.get("promedio"))
            print("----------------------------------")

def suma(valores_suma):
    print()
    suma = 0
    promedio = 0
    if valores_suma == "edad":
            for dato in arreglo:
                suma = suma + dato.get("edad")
            print("La suma total de las edades es: " + str(suma))
            
            print("----------------------------------")
    else:
            for dato in arreglo:
                promedio = promedio + dato.get("promedio")
            print("La suma total de los promedios es: " + str(promedio))
            
            print("----------------------------------")

def reporte(numero_reporte):
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "reporte.html")
    with  open(path, 'w+') as file_reporte:
        file_reporte.write(report.codinicio)
        for i in range(int(numero_reporte)):    
            file_reporte.write("<tr>") 
            file_reporte.write("<td>" + str(i+1) + "</td>")                                    
            for atributo in allatrib:
                file_reporte.write("<td>" + str(arreglo[i].get(atributo)) + "</td>" )
            file_reporte.write("</tr>")
        file_reporte.write(report.final_hmtl)
        file_reporte.close()
    webbrowser.open_new(path)
    print("Reporte Creado con Exito")

main()
