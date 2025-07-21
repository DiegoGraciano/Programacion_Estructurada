import os 


def borrarPantalla():
    os.system("cls")

def esperarTecla():
    input("\U0001F552 Presiona una tecla para continuar...")

def menu_principal():
     borrarPantalla()
     print("\n\t\t\t\033[94m\033[1m...::::: 📞 Sistema de Gestion de Agenda de Contactos 👤 :::::...\n\033[0m"
          "\n\t\t\033[1m1. \U0001F4DD Agregar contacto \n"
          "\t\t2. \U0001F50D Mostrar todos los contactos \n"
          "\t\t3. \u2795 Buscar contactos por nombre \n"
          "\t\t4. \u2795 Modificar contacto \n"
          "\t\t5. \u2795 Eliminar contacto \n"
          "\t\t6. \U0001F6AA Salir")
     op = int(input("\n\t\tIngresa una opción: \033[0m"))
     return op

def agregar_contacto(agenda):
    borrarPantalla()
    print("..::: Agregar Contactos :::..")
    nombre=input("Nombre del contaco: ").upper().strip()
   
    if nombre in agenda:
        print("\n\t El contacto ya existe...")
    else:
        tel=input("Telefono: ").strip()
        email=input("E-mail: ").lower().strip()
        #Agregar atributo al diccionario con los valores de tel e email
        agenda[nombre]=[tel,email]
        print("\n\t\t .::Accion Realizada::..")

def Mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t ...:::Mostrar Contactos:::...")
    if not agenda:
        print("\n\t\t No Existe contactos en la agenda")
    else:
        for nombre,datos in agenda:
            print(f" {"Nombre:"+nombre}\n\t{"Telefonos: "+datos[0]}\n\t{"E-mail: "+datos[1]}")

def Modificar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t \U0001F501 .::Modificar Contactos::. \U0001F501")
    if not agenda:
        print("\n\t\t \u26A0 No existen contactos en la agenda \u26A0")
    else:
        nom=input("Ingresa el nombre del contacto que desea modificar: ").upper().strip()
        encontro=0
        for nombre,datos in agenda.items():
            if nombre==nom:
                print(f"El contacto actual es: \n\t{nombre} \n\t{'telefono:'+datos[0]}\n\t{'E-mail:'+datos[1]}")
                tel=input("Ingrese el nuevo numero de telefono: ")
                mail=input("Ingrese el nuevo e-mail: ")
                datos[0]=tel
                datos[1]=mail
                encontro+=1
        if encontro==0:
            print(f"\n\t \u274C No se encontro un contacto con el nombre {nom} para modificar \u274C")

def Eliminar_contactos(agenda):
    borrarPantalla()
    print("\n\t\U0001F4DB .:: Borrar todas las películas ::.")
    res = input("\u26A0 ¿Deseas borrar todas las películas del sistema? (si/no): ").lower()
    if res == "si":
        agenda.clear()
        print("\u2705 Ya se vaciaron todas las películas")
 




    
