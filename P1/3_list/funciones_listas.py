'''
List(Array)
Son colecciones o conjunto de datos/valores bajo 
un mismo nombre para acceder a los valors se 
hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion oredenada y
modificable.Permite miembros duplicados

'''
import os
os.system("cls")

#Funciones mas comunes en las listas 
paises=["Mexico","Brasil","España","Canada"]
numeros=[23,12,100,34]

#Ordenar acendente mente
print(numeros)
numeros.sort()
print(numeros)
print(paises)
paises.sort()
print(paises)

#Añadir o ingresar elementos a una lista

#1er._forma
print(paises)
paises.append("Honduras")
#2da._forma
paises.insert(1,"Honduras")
print(paises)

#Eliminar o Quitar elemnto de una lista

#1er._forma
paises.pop(1)
print(paises)
#2da._forma
paises.remove("Honduras")
print(paises)

#Buscar elemento dentro de una lista

resp="Brasil" in paises
if resp:
    print("Si encontre el pais")
else:
     print("No encontre el pais")

for i in range(0,len(paises)):
      paises_buscar=input(0,len(paises))
      if paises[i]=="Brasil":
            print("Si")
      else:
            print("No")


 
#Cuantas veces        
print(f"Este numero 12 aparece{numeros.count(12)} vez 0 veces")

numeros.append(12)
print(f"Este numero 12 aparece{numeros.count(12)} vez 0 veces")


indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)


for i in paises:
      print(i)

    
for i in range(0,len(paises)):
      print[i]
      
# unir contenido de listas

print(paises)
print(numeros)
paises.extend(numeros)
