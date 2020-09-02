# SimpleQL

SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su propósito es facilitar la búsqueda de registros completos en archivos json.


## Comandos 
Todos los comandos son **Case insensitive** 


* ## CARGAR

Con este comando es posible cargar uno o varios archivos a memoria ,el patrón que sigue este comando es:

```bash
cargar file1.json
CARGAR file1.json, file2.json, file3.json, ..., fileN.json
```
[Estructura JSON](https://drive.google.com/file/d/11P9Ms_1mJw5y6JSreRBsOOPOWhPQe3Yt/view)

* ## SELECCIONAR
Permite seleccionar uno o más registros o atributos de los mismos con base en condiciones simples que pueden aplicarse a los atributos de los mismos. El patrón que sigue este comando es:

```bash
SELECCIONAR *
SELECCIONAR * DONDE promedio = 61.61
SELECCIONAR nombre, edad, activo DONDE nombre  = "name"
```
El (*) se utiliza para seleccionar todos los atributos.

Los atributos pueden estar o no en orden.
 
* ## MAXIMO & MINIMO
Permite encontrar el valor máximo o mínimo que se encuentre en el atributo de uno de los registros del conjunto en memoria. El patrón que sigue este comando es:

```bash
MAXIMO edad               |  MINIMO edad
MAXIMO promedio           |  MINIMO promedio
```

* ## SUMA
Permite obtener la suma de todos los valores de un atributo especificado en el comando. El patrón que sigue este comando es:

```bash
SUMA edad               
SUMA promedio         
```
* ## CUENTA
Permite contar el número de registros que se han cargado a memoria.
El patrón que sigue este comando es:
```bash
CUENTA        
```

* ## REPORTAR
Este comando permite crear un reporte en html que contiene N cantidad de
registros. 
```bash
REPORTAR N
```


* Todas los comandos a excepcion de **REPORTAR** imprimiran el resultado en consola.
### PRACTICA_LFP
201700522
