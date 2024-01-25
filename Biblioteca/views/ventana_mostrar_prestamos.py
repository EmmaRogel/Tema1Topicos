import tkinter as tk
from views import ventana_agregar_alumno
class MostrarPrestamos():
    def __init__(self, ventana_manager) :
        self.ventana_manager = ventana_manager
        self.ventana_mostrar_alumnos= tk.Toplevel()
        self.ventana_mostrar_alumnos.title("Mostrar todos los Libros")
        tk.Label(self.ventana_mostrar_alumnos, text="Lista Libros Prestados por Alumno").grid(column=1, row=0,padx=20 ,pady=10)
        
        alumnos = ventana_agregar_alumno.lista_alumnos
        if len(alumnos) == 0:
            tk.Label(self.ventana_mostrar_alumnos, text="No existen Alumnos registrados").grid(column=1, row=1,padx=20 ,pady=10)
        else:
            i=0
            for alumno in alumnos:
                i=i+1
                tk.Label(self.ventana_mostrar_alumnos, text="Nombre:").grid(column=1,padx=20 )
                tk.Label(self.ventana_mostrar_alumnos, text=alumno.nombre).grid(column=2,padx=20 )
                tk.Label(self.ventana_mostrar_alumnos, text="Apellidos:").grid(column=1,padx=20 )
                tk.Label(self.ventana_mostrar_alumnos, text=alumno.apellido).grid(column=2,padx=20 )
                tk.Label(self.ventana_mostrar_alumnos, text="dni:").grid(column=1,padx=20 )
                tk.Label(self.ventana_mostrar_alumnos, text=alumno.dni).grid(column=2,padx=20 )
                tk.Label(self.ventana_mostrar_alumnos, text="Libros Prestados").grid(column=2,padx=20 )
                for libro in alumno.libros_prestados:
                    tk.Label(self.ventana_mostrar_alumnos, text=libro).grid(column=2)
                tk.Label(self.ventana_mostrar_alumnos, text="***********************").grid(column=1,padx=20 ,pady=10)

        tk.Button(self.ventana_mostrar_alumnos, text="Regresar", command=self.cerrar_y_mostrar_principal).grid(column=4, row= 1,padx=20 ,pady=10)

                # asdsa
    def cerrar_y_mostrar_principal(self):
        self.ventana_mostrar_alumnos.destroy()
        self.ventana_manager.mostrar_ventana_principal()