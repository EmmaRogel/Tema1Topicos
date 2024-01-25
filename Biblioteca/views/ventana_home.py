import tkinter as tk
from ventana_manager import VentanaManager
import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient


class VentanaHome:
    def __init__(self, ventana_manager):
        self.ventana_manager = ventana_manager
        self.ventana_home = tk.Tk()
        self.ventana_home.title("Menú Principal")

        try:
            username = "bdata"
            password = "1234"
            cluster_url = "biblioteca.j9zcdza.mongodb.net"

            connection_string = f"mongodb+srv://{username}:{password}@{cluster_url}/test?retryWrites=true&w=majority"

            client = MongoClient(connection_string)

            messagebox.showinfo(
                "Conexión Exitosa", "Conexión a la Base de Datos exitosa."
            )
            screen_width = self.ventana_home.winfo_screenwidth()
            screen_height = self.ventana_home.winfo_screenheight()
            x_position = int((screen_width - 250) / 2)
            y_position = int((screen_height - 180) / 2)
            self.ventana_home.geometry(f"250x180+{x_position}+{y_position}")

            tk.Label(self.ventana_home, text="").grid(row=0, column=0)

            tk.Label(self.ventana_home, text="").grid(row=1, column=0)
            tk.Label(self.ventana_home, text="").grid(row=1, column=1)
            tk.Button(
                self.ventana_home,
                text="LIBROS",
                command=self.abrir_ventana_mostrar_libros,
            ).grid(row=1, column=3, sticky="nsew", padx=20, pady=20)

            tk.Button(
                self.ventana_home,
                text="ALUMNOS",
                command=self.abrir_ventana_mostrar_alumno,
            ).grid(row=1, column=5, sticky="nsew", padx=20, pady=20)

            tk.Button(
                self.ventana_home,
                text="PRÉSTAMOS",
                command=self.abrir_hacer_prestamo,
            ).grid(row=2, column=3, sticky="nsew", padx=20, pady=20)

            tk.Button(
                self.ventana_home, text="SALIR", command=self.finalizar_aplicacion
            ).grid(row=2, column=5, sticky="nsew", padx=20, pady=20)

            client.close()

        except Exception as e:
            error_message = f"No se pudo conectar a la Base de Datos.\nError: {str(e)}"
            print(error_message)
            messagebox.showerror("Error de Conexión", error_message)

    def finalizar_aplicacion(self):
        self.ventana_home.destroy()

    def iniciar_aplicacion(self):
        self.ventana_home.mainloop()

    def ocultar_ventana(self):
        self.ventana_home.withdraw()

    def mostrar_ventana(self):
        self.ventana_home.deiconify()

    def abrir_nueva_ventana(self):
        self.ocultar_ventana()
        self.ventana_manager.abrir_nueva_ventana()

    def abrir_ventana_mostrar_libros(self):
        self.ocultar_ventana()
        self.ventana_manager.abrir_mostrar_libro()

    def abrir_ventana_agregar_alumno(self):
        self.ocultar_ventana()
        self.ventana_manager.abrir_agregar_alumno()

    def abrir_ventana_mostrar_alumno(self):
        self.ocultar_ventana()
        self.ventana_manager.abrir_mostrar_alumnos()

    def abrir_hacer_prestamo(self):
        self.ocultar_ventana()
        self.ventana_manager.abrir_mostrar_prestamos()


if __name__ == "__main__":
    ventana_manager = VentanaManager()
    ventana_principal = VentanaHome(ventana_manager)
    ventana_principal.iniciar_aplicacion()
