import os 
lista=[]

def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\U0001F552 Presiona una tecla para continuar...")

def menu_principal():
     borrarPantalla()
     print("\n\t\t\t\033[94m\033[1m...::::: \U0001F4C2 MENÚ \U0001F4C2 :::::...\n\033[0m"
          "\t\t\033[1m1. \U0001F4DD Agregar Estudiante \n"
          "\t\t2. \U0001F50D Mostrar \n"
          "\t\t3. \u2795 Calcular Promedio \n"
          "\t\t4. \U0001F6AA Salir")
     op = int(input("\n\t\tIngresa una opción: \033[0m"))
     return op


            
def anadir_alumnos(lista):
    borrarPantalla()
    print("\n\t\U0001F4DD ...::: Añadir Alumno :::... \U0001F4DD ")
    nombre=input("\U0001F464 Nombre del Alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input("\U0001F4DD Calificacion del parcial: "))
                if cal>0 and cal<11:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("\u274C ingrese un numero valido")
            except ValueError:
                print("\u274C Ingresa un valor numerico")

    lista.append([nombre]+calificaciones)
    print("\u2705 Accion Realizada Con Exito")

def Consultar_alumnos(lista):
    borrarPantalla()
    print("\U0001F50D ..:: Alumnos ::..")
    if len(lista) > 0:
        print(f"\U0001F464 {'Nombre':<15}\U0001F4DD {'calf.1':<10}\U0001F4DD {'calf.2':<10}\U0001F4DD {'calf.3':<10}")
        print(f"{'-'*40}")
        for fila in lista:
            print(f"\t\U0001F464 {fila[0]:<15} \U0001F4DD{fila[1]:<10}\U0001F4DD {fila[2]:<10}\U0001F4DD {fila[3]:<10}")
        print(f"{'-'*30}")
        cuantos=len(lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("\u274C No hay Alumnos en el sistema")

def Promedio_alumnos(lista):
    borrarPantalla()
    print("\n\t\U0001F4DB .:: Promedio Calificaciones ::.")
    if len(lista) > 0:
        print(f"{'Alumnos':<15}-{'Promedio':<10}")
        print(f"{'-'*30}")
        for fila in lista:
            nombre=fila[0]
            promedio=sum(fila[1:])/3
            print(f"{nombre:<15}{promedio:.2f}")
            promedio_grupal+=promedio
        print(f"{'-'*30}")
        promedio_grupal=promedio_grupal/len(lista)
        print(f"El promedio grupal es: {promedio_grupal:.2}")
    
        
    else:
        print("\u274C No hay Alumnos en el sistema")
    







     