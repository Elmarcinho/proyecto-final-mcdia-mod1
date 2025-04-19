import os


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


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
