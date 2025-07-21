'''
dict.-
es un tipo de datos que se utiliza para almacenar datos de 
diferente tipo de datos pero en lugar de tener como as listas
indices numericos tiene alfanumericos.Es decir es algo parecido
como los objetos

Tmabien se conoce como un arreglo asiativo u ibjeto JSON

El diccionarioe es una coleccion ordenada y modificable,No
hay miembros duplicados.
'''
import os 
os.system("cls")

#paises={"Mexico","Brasil","Canada","España"}

#Dict o objeto
paises_mexico={
    "nombre":"Mexico",
    "capiptal:":"CDMEX",
    "poblacion:":"1200000",
    "idiomas:":"español",
    "status":True
    }

paises_brasil={
    "nombre: ":"Brasil",
    "capiptal:":"Brasilia",
    "poblacion:":"1000000",
    "idiomas:":"portugues",
    "status":True
    }

paises_canada={
    "nombre: ":"Canada",
    "capiptal:":"Ottawa",
    "poblacion:":"91000000",
    "idiomas:":["ingles","frances"],
    "status":True
    }

alumnos1={
    "nombre":"TUFU",
    "apellido_paterno":"Gonzalez",
    "apellido_2":"Cabral",
    "carerra":"TI",
    "area":"software multiplataforma",
    "modalidad":"Bilingue",
    "Matricula":"12345678",
    "semestre":"2"
    }


for i in alumnos1:
    print(f"{i}={alumnos1[i]}")

alumnos1["telefono"]="6181843769"
for i in alumnos1:
    print(f"{i}={alumnos1[i]}")

