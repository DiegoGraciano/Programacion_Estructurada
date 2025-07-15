'''Crear un proyecto que permita adminsitrar peliculas.colocar un menu de opciones para agregar 
eliminar modificar y consultar peliculas

notas:
1._Utilizar funciones y mandar a llamar desde otros archivo
2._Utilizar listas para los nombres de peliculas

'''
import peliculas
import os
os.system("cls")

def menu(op):
        match op:
            case 1:
                peliculas.borrarPantalla()
                peliculas.anadir_peliculas()
                peliculas.esperarTecla()
                
            case 2:
                peliculas.borrarPantalla()
                peliculas.Eliminar_peliculas()
                peliculas.esperarTecla()
            case 3:
                peliculas.borrarPantalla()
                peliculas.Modificar_peliculas()
                peliculas.esperarTecla()
            case 4:
                peliculas.borrarPantalla()
                peliculas()
                peliculas.esperarTecla()
            case 5:
                op=False
            case _:
                return "NONI WE"

op=True
while op:
    print("\t...:::::MENU:::::...\n1._Añadir\n2._Eliminar\n3._Modificar\n4._Comsultar\n5._Salir")
    op=int(input("\t Ingresa un opcion: "))
    menu(op)
    
    
    
    
    








