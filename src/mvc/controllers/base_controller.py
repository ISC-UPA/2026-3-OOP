import mysql.connector


class BaseController:
    """Ciclo del menú que comparten todos los controladores."""

    def __init__(self, repository, view) -> None:
        self.repository = repository
        self.view = view
        self.actions = {}  # cada controlador lo llena: {"1": self.add, "2": self.delete, ...}

    def run(self) -> None:
        while True:
            option = self.view.ask_option()  # presenta menu y captura opcion
            if option == "0":
                break
            action = self.actions.get(option)
            if action is None:
                self.view.show_error("Opción no válida")
                continue
            try:
                action()
            except mysql.connector.IntegrityError:
                self.view.show_error("No se puede: el registro está relacionado con otros (por ejemplo, tiene órdenes).")
            except mysql.connector.Error as error:
                self.view.show_error(f"Error de base de datos: {error}")
