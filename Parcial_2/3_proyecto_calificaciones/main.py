'''
Proyecto 3

Crear un proyecto que permita adminsitrar calificaciones.colocar un menu de opciones para agregar, mostrar y calculara promedio calficaciones de estudiantes.

notas:
1._Utilizar funciones y mandar a llamar desde otros archivo.
2._Utilizar listas bidimencional para almacenar el nombre del alumno asi como sus tres calificaciones.

'''
import cali
import os
os.system("cls")



def menu():
    datos=[]
    op = True
    while op:
        op=cali.menu_principal()
        match op:
            case 1:
                cali.anadir_alumnos(datos)
                cali.esperarTecla()
            case 2:
                cali.Consultar_alumnos(datos)
                cali.esperarTecla()
            case 3:
                cali.Promedio_alumnos(datos)
                cali.esperarTecla()
            case 4:
                print("\U0001F6AA Saliendo del programa...")
                resp = False
            case _:
                print("\033[91m\u274C Opción inválida.\033[30m")


if __name__=="__main__":
    menu()







