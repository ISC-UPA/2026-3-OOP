import os, sys
from pathlib import Path

# Add the project root so this file can also be run directly.
sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from src.mvc.views.base_view import BaseView

class MainView(BaseView):
    def ask_option(self) -> str:
        print("""
========== Menú Principal ==========
1. Empleados
2. Productos
0. Salir
====================================""")
        return input("Seleccione una opción: ").strip()
        
def main():
    MainView().show_message("Hola Mundo!. . .")
    MainView().ask_option()

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    main()
    print("\n. . . H e c h o")
    