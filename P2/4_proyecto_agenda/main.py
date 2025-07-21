import agenda
import os
os.system("cls")

def menu():
    agenda_contactos={}
    op = True
    while op:
        op=agenda.menu_principal()
        match op:
            case 1:
                agenda.agregar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case 2:
                agenda.mostrar_contactos(agenda_contactos)
                agenda.esperarTecla()
            case 3:
                agenda.buscar_contacto(agenda_contactos)
                agenda.esperarTecla()
            case 4:
                agenda.modificar_contactos(agenda_contactos)
                agenda.esperarTecla()
            case 5:
                agenda.eliminar_contactos(agenda_contactos)
                agenda.esperarTecla()    
            case 6:
                print("\U0001F6AA Saliendo del programa...")
                resp = False
            case _:
                print("\033[91m\u274C Opción inválida.\033[30m")


if __name__=="__main__":
    menu()