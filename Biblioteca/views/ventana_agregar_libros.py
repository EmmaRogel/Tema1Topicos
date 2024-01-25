import tkinter as tk
from controllers import book
lista_libros =[]
class AgregarLibros:
    def __init__(self, ventana_manager):
        self.ventana_manager = ventana_manager
        self.ventana_agregar_Libro = tk.Toplevel()
        self.ventana_agregar_Libro.geometry("250x400")
        self.titulo =tk.StringVar()
        self.autor =tk.StringVar()
        self.ubicacion =tk.StringVar()

        self.ventana_agregar_Libro.title("Agregar Libro")
        tk.Label(self.ventana_agregar_Libro, text="Agrega nuevos libros a la Bilbioteca").grid(column=1, row=0,padx=20 ,pady=10)

        # Etiqueta y campo de entrada para el título del libro
        tk.Label(self.ventana_agregar_Libro, text="Título del libro:").grid(column=1, row=2,padx=20 ,pady=10)
        tk.Entry(self.ventana_agregar_Libro, textvariable=self.titulo).grid(column=1, row=3,padx=20 ,pady=10)

        # Etiqueta y campo de entrada para el autor del libro
        tk.Label(self.ventana_agregar_Libro, text="Autor del libro:").grid(column=1, row=4,padx=20 ,pady=10)

        tk.Entry(self.ventana_agregar_Libro, textvariable=self.autor).grid(column=1, row=5,padx=20 ,pady=10)

        # Etiqueta y campo de entrada para la ubicación del libro
        tk.Label(self.ventana_agregar_Libro, text="Ubicación del libro:").grid(column=1, row=6,padx=20 ,pady=10)

        tk.Entry(self.ventana_agregar_Libro, textvariable=self.ubicacion).grid(column=1, row=7,padx=20 ,pady=10)

        # Botón para cerrar la nueva ventana y mostrar la ventana principal
        tk.Button(self.ventana_agregar_Libro, text="Agregar", command= self.agregar_libro).grid(column=1, row=8,padx=20 ,pady=10)

        tk.Button(self.ventana_agregar_Libro, text="Regresar", command=self.cerrar_y_mostrar_principal).grid(column=1, row=9,padx=20 ,pady=10)

    def agregar_libro(self):
        titulo = self.titulo.get()
        autor = self.autor.get()
        ubicacion = self.ubicacion.get()
        libros = lista_libros
        nuevo_libro = book.Libro(titulo, autor, ubicacion)
        libros.append(nuevo_libro)
        print(libros)

    def cerrar_y_mostrar_principal(self):
        self.ventana_agregar_Libro.destroy()
        self.ventana_manager.mostrar_ventana_principal()

    