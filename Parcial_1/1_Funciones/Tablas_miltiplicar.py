'''
Crear un programa que calcule e imprime cualquier tabla de multiplicar 

con dunciones y regrese valor y utilice parametros
'''
regre=0

def tabladfor(num):
    for i in range (1,11): 
        multi=num*i
        regre=0
        regre=print((f"{num} x {i} = {multi}"))
    
    
    return regre

def tablaswhile():
    num=int(input("Dame un numero de la tabla de multiplicar: "))
    i=1
    while i<=10:
        multi=num*1
        print(f"{num} x {i} = {multi}")
        i+=1


num=int(input("Dame un numero de la tabla de multiplicar: "))
tabladfor(num)

print(regre)

