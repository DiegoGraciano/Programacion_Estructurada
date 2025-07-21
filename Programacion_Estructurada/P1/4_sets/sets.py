'''
Es un tipo de dato para tener una coleccion de valores no tiene ni
indice ni orden

Set es unz coleccion desordenada inmutable y no indexada
no hay miembros duplicados
'''
import os 
os.system("cls")

print("--------------------------")
personas={"Ramiro","Choche","Lupe"}
print(personas)
print("--------------------------")
personas.add("peje")
print(personas)
'''print("--------------------------")
personas.pop()
print(personas)
print("--------------------------")
personas.clear()
print(personas)
print("--------------------------")'''

print("")
varios={3.12,3,True,"Hola"}
print(varios)

#Ejemplo. crear un programa que solicite los correos de los alumnos de la utd en una lista y posteriormente mostrar en pantalla los email sin duplicados
os.system("cls")

opc="si"
emails={}
while opc == "si":
    emails.append(input("Dame un email"))
    print(emails)
    opc=input("Deseas solcitar otro email? (si/no)").lower()

print(emails)
set1=set(emails)
print(set1)
emails=list(set1)
print(emails)
