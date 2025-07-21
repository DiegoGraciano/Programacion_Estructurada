import os 
peliculas=["Fornite OG","R69","Pornite"]
def borrarPantalla():
        os.system("cls")

def esperarTecla():
    input("Presiona una tecla para continuar...")

def anadir_peliculas():
    nombre=input("Ingrese el nombre de la pelicula a Añadir: ")
    peliculas.append(nombre)
    print("Se agrego una pelicula correctamente")
    print(peliculas)
            

def Eliminar_peliculas():
    print(peliculas)
    print("")
    nombre=input("Ingrese el nombre de la pelicula a Eliminar: ")
    peliculas.remove(nombre)
    print("Pelicula eliminada....")
    print(peliculas)
    

def Modificar_peliculas():
    print(peliculas)
    nombre=input("Ingrese el nombre de la pelicula a Modificar: ")
    print(peliculas)
    peliculas.replace(nombre)

def Consultar_peliculas():
    nombre=input("Ingrese el numero para la consulta: ")
    print(peliculas)

    resp=nombre in peliculas

    if resp:
        print("Si encontre la pelicula")
    else:
        print("No encontre la pelicula")

    for i in range(0,len(peliculas)):
        if peliculas[i]==nombre:
                print("Si")
        else:
                print("No")
        