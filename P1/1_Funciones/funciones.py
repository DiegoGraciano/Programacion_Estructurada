'''
Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor


sintaxis:

'''

#1.- Funcion que no recibe parametros y no regresa valor
def resivirDatos1():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    print(f"Soy funcion 1: El nombre es:{nombre} y su telefono es: {telefono}")


#3.- Funcion que recibe parametros y no regresa valor
def resivirDatos3(nombre,telefono):
    nombre=nombre
    telefono=telefono
    print(f"Soy funcion 3: El nombre es:{nombre} y su telefono es: {telefono}")

nombre=input("Nombre: ")
telefono=input("Telefono: ")


#2.- Funcion que no recibe parametros y regresa valor
def resivirDatos2():
    nombre=input("Nombre: ")
    telefono=input("Telefono: ")
    return nombre,telefono


#4.- Funcion que recibe parametros y regresa valor
def resivirDatos4(nombre,telefono):
    nombre=nombre
    telefono=telefono
    return nombre,telefono

#Llamar mis funciones

resivirDatos1()

nombre3=input("Nombre: ")
telefono3=input("Telefono: ")
resivirDatos3(nombre3,telefono3)

nom2,tel2=resivirDatos2()
print(f"Soy funcion 3: El nombre es:{nom2} y su telefono es: {tel2}")

nombre4=input("Nombre: ")
telefono4=input("Telefono: ")
nom4,tel4=resivirDatos4(nombre4,telefono4)
print(f"Soy funcion 3: El nombre es:{nom4} y su telefono es: {tel4}")



