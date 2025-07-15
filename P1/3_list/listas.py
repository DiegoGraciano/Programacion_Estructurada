#Ejemplo 1 Crear uan lista de numeros e imprimir el contenido
import os
os.system("cls")

print("------------------")

numeros=[1,42,28,12,]
print(numeros)

print("------------------")

for i in numeros:
    print(i)

print("------------------")

for i in range(0,len(numeros)):
    print(numeros[i])

print("----------------------------------")

#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palabras=["pollos","patos","ovejas","marranos"]
print(palabras)

print("----------------------------------")

palabra_buscar=input("Dame la palabra a buscar:")

print("----------------1ra._Forma------------------")
print(f"El numero de veces que se encontro cuantas veces: {palabras.count(palabra_buscar)}")
if palabra_buscar in palabras:
    print(f"Si encontro la palabra")
    
else:
    print(f"No encontro la palabra")

print("---------------2da._Forma-------------------")

encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True

if encontro:
    print(f"Si encontro la palabra")
else:
    print(f"No encontro la palabra")

print("----------------3er._Forma------------------") 

encontro=False
for i in palabras:
    if i==palabra_buscar:
        encontro=True

if encontro:
    print(f"Si encontro la palabra")
else:
    print(f"No encontro la palabra")

print("----------------------------------")
input("Oprima tecla....")
os.system("cls")
#Ejemplo 3 Añadir elementos a la lista
print("----------------------------------")
numeros=[]
print(numeros)

opc=True
while opc:
    numero=float(input("Ingresa un numero a añadir: "))
    numeros.append(numero)
    resp=input("¿Deseas agregar otro numero?").lower()
    if resp=="si":
        opc=True
    else:
        opc=False

print(numeros)
input("Oprima tecla....")

print("----------------------------------")

#Ejemplo 4 Crear una lista multidimencional que sea una agenda

agenda=[
    ["Carlos","618183769"],
    ["jose","618168452"],
    ["Martin","618555777"]
]
print(agenda)

print("----------------------------------")

for i in agenda:
    print(i)

print("----------------------------------")

for r in range(0,3):
    for c in range(0,2):
        print(f"{agenda[r][c]}")

print("----------------------------------")

cadena=""
for r in range(0,3):
    for c in range(0,2):
        cadena+=f"{agenda[r][c]},"
        cadena+="\n"
print(cadena)
