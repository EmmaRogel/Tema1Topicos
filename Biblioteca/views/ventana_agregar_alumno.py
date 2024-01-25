import tkinter as tk
from controllers import student
lista_alumnos =[]
class AgregarAlumno:
    def __init__(self, ventana_manager):
        self.ventana_manager = ventana_manager
        self. ventana_agregar_alumno = tk.Toplevel()
        self.nombre = tk.StringVar()
        self.apellido = tk.StringVar()
        self.dni = tk.StringVar()
        self.libros_prestados = tk.StringVar()

        self.ventana_agregar_alumno.title("Agregar Alumno")
        tk.Label(self.ventana_agregar_alumno, text="Agregar Alumno")

        
        # Etiqueta y campo de entrada para el título del libro
        tk.Label(self.ventana_agregar_alumno, text="Nombre:").grid(column=1, row=2,padx=20 ,pady=10)
        tk.Entry(self.ventana_agregar_alumno, textvariable=self.nombre).grid(column=1, row=3,padx=20 ,pady=10)

        # Etiqueta y campo de entrada para el autor del libro
        tk.Label(self.ventana_agregar_alumno, text="Apellidos:").grid(column=1, row=4,padx=20 ,pady=10)

        tk.Entry(self.ventana_agregar_alumno, textvariable=self.apellido).grid(column=1, row=5,padx=20 ,pady=10)

        # Etiqueta y campo de entrada para la ubicación del libro
        tk.Label(self.ventana_agregar_alumno, text="dni:").grid(column=1, row=6,padx=20 ,pady=10)

        tk.Entry(self.ventana_agregar_alumno, textvariable=self.dni).grid(column=1, row=7,padx=20 ,pady=10)
        
        tk.Label(self.ventana_agregar_alumno, text="dni:").grid(column=1, row=6,padx=20 ,pady=10)

        tk.Entry(self.ventana_agregar_alumno, textvariable=self.dni).grid(column=1, row=7,padx=20 ,pady=10)

        # Botón para cerrar la nueva ventana y mostrar la ventana principal
        tk.Button(self.ventana_agregar_alumno, text="Agregar", command= self.agregar_alumno).grid(column=1, row=8,padx=20 ,pady=10)

        tk.Button(self.ventana_agregar_alumno, text="Regresar", command=self.cerrar_y_mostrar_principal).grid(column=1, row=9,padx=20 ,pady=10)

    def agregar_alumno(self):
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        dni = self.dni.get()
        alumnos = lista_alumnos
        nuevo_alumno = student.Alumno(nombre, apellido, dni)
        alumnos.append(nuevo_alumno)
        print(alumnos)

    def cerrar_y_mostrar_principal(self):
        self.ventana_agregar_alumno.destroy()
        self.ventana_manager.mostrar_ventana_principal()
