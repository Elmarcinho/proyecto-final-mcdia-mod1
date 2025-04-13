import os
from time import sleep
from utils.menu import Colors


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_option():
    while True:
        try:
            option = int(input(Colors.WHITE + "Seleccione una opción: " + Colors.RESET))
            if 0 <= option <= 5:
                return option
            else:
                print(Colors.RED + "Opción no válida. Intente de nuevo." + Colors.RESET)
        except ValueError:
            print(Colors.RED + "Entrada inválida. Debe ser un número." + Colors.RESET)


def menu():
    while True:
        clear_screen()
        print(Colors.BLUE + "="*50 + Colors.RESET)
        print(Colors.BOLD + Colors.CYAN + "SISTEMA DE GESTIÓN DE IMÁGENES".center(50) + Colors.RESET)
        print(Colors.BLUE + "="*50 + Colors.RESET)
        print()
        print(Colors.YELLOW + "MENÚ PRINCIPAL" + Colors.RESET)
        print("1. Registrar nueva imagen")
        print("2. Modificar imagen")
        print("3. Eliminar imagen")
        print("4. Listar imágenes")
        print(Colors.RED + "0. " + Colors.RESET + "Salir")
        print(Colors.BLUE + "-"*50 + Colors.RESET)

        option = get_option()
        
        if option == 1:
            print()
            image = input("Nombre de la imagen: ")
            print(Colors.GREEN + f"Imagen '{image}' registrada correctamente!" + Colors.RESET)
            sleep(2)
            input("\nPresione Enter para continuar...")
        elif option == 2:
            print()
            image = input("Nuevo nombre de la imagen: ")
            print(Colors.GREEN + f"Imagen renombrada a '{image}' correctamente!" + Colors.RESET)
            sleep(2)
            input("\nPresione Enter para continuar...")
        elif option == 3:
            print()
            id_imagen = input("Ingrese el Identificador de la imagen a eliminar: ")
            print(Colors.GREEN + f"Imagen con ID '{id_imagen}' eliminada correctamente!" + Colors.RESET)
            sleep(2)
            input("\nPresione Enter para continuar...")
        elif option == 4:
            print("Lista de imágenes:")
            sleep(2)
            input("\nPresione Enter para continuar...")
            # Agregar lógica para listar imágenes almacenadas
        elif option == 0:
            print(Colors.YELLOW + "\nSaliendo del sistema..." + Colors.RESET)
            sleep(1)
            print(Colors.GREEN + "¡Hasta pronto!" + Colors.RESET)
            sleep(1)
            clear_screen()
            break
        else:
            print(Colors.RED +"Opción no válida, por favor intente nuevamente"+ Colors.RESET)


if __name__ == "__main__":
    menu()
