from time import sleep

from controllers import ImageController
from utils import Colors, clear_screen, get_option

image_controller = ImageController()


def menu():
    while True:
        clear_screen()
        print(Colors.BLUE + "=" * 50 + Colors.RESET)
        print(
            Colors.BOLD
            + Colors.CYAN
            + "SISTEMA DE GESTIÓN DE IMÁGENES".center(50)
            + Colors.RESET
        )
        print(Colors.BLUE + "=" * 50 + Colors.RESET)
        print()
        print(Colors.YELLOW + "MENÚ PRINCIPAL" + Colors.RESET)
        print("1. Registrar nueva imagen")
        print("2. Modificar imagen")
        print("3. Eliminar imagen")
        print("4. Listar imágenes")
        print(Colors.RED + "0. " + Colors.RESET + "Salir")
        print(Colors.BLUE + "-" * 50 + Colors.RESET)

        option = get_option()

        if option == 1:
            print()
            file_name = input("Nombre de la imagen: ").strip()
            size = input("Tamaño de la imagen: ")
            url = input("URL de la imagen: ")
            route = image_controller.register_image(file_name, size, url)
            if route:
                print(
                    Colors.GREEN
                    + f"Imagen: '{file_name}' registrada correctamente!\nRuta1: {route[0]}\nRuta2: {route[1]}"
                    + Colors.RESET
                )
            else:
                print(Colors.RED + "No se pudo registrar la imagen" + Colors.RESET)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 2:
            print()
            id_image = int(input("Ingrese el 'ID' de la imagen a modificar: "))
            file_name = input("Nuevo nombre de la imagen: ")
            size = input("Nuevo tamaño de la imagen: ")
            url = input("Nueva URL de la imagen: ")

            if image_controller.modify_image(id_image, file_name, size, url):
                print(
                    Colors.GREEN
                    + f"Imagen renombrada a '{file_name}' correctamente!"
                    + Colors.RESET
                )
            else:
                print(Colors.RED + "Error: Imagen no encontrada." + Colors.RESET)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 3:
            print()
            id_imagen = int(input("Ingrese el 'ID' de la imagen a eliminar: "))

            if image_controller.delete_image(id_imagen):
                print(
                    Colors.GREEN
                    + f"Imagen con ID '{id_imagen}' eliminada correctamente!"
                    + Colors.RESET
                )
            else:
                print(Colors.RED + "Error: Imagen no encontrada." + Colors.RESET)
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 4:
            print("Lista de imágenes:")
            image_controller.list_images()
            sleep(1)
            input("\nPresione Enter para volver al menú principal...")
        elif option == 0:
            print(Colors.YELLOW + "\nSaliendo del sistema..." + Colors.RESET)
            sleep(1)
            print(Colors.GREEN + "¡Hasta pronto!" + Colors.RESET)
            sleep(1)
            clear_screen()
            break
        else:
            print(
                Colors.RED
                + "Opción no válida, por favor intente nuevamente"
                + Colors.RESET
            )


if __name__ == "__main__":
    menu()
