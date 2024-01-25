import tkinter as tk
from home_view import main

if __name__ == "__main__":
    ventana_manager = main()
    ventana_manager.iniciar_aplicacion()



















# from controllers import author, book, shelf, student, library
# autor1 = author.Autor("J.K.", "Rowling", "Británica")
# libro1 = book.Libro("Harry Potter y la Piedra Filosofal", autor1, "Estantería 1")
# libro2 = book.Libro("Harry Potter y la Piedra Filosofal II", autor1, "Estantería 1")
# alumno1 = student.Alumno("Juan", "Pérez", "12345678")
# estante1 = shelf.Estante()
# biblioteca = library.Biblioteca()

# # Agregar estante a la biblioteca
# biblioteca.agregar_estante("Fantasía")

# # Agregar libro al estante
# biblioteca.agregar_libro_a_estante(libro1, "Fantasía")

# # Obtener el inventario de la biblioteca
# inventario = biblioteca.obtener_inventario()
# print("Inventario de la biblioteca:")
# for estante, libros in inventario.items():
#     print(f"{estante}:")
#     for libro in libros:
#         print(f"  {libro}")

# # Agregar alumno
# biblioteca.agregar_alumno(alumno1.dni, alumno1.nombre, alumno1.apellido)

# # Prestar libro a un alumno
# biblioteca.prestar_libro(libro1, alumno1.dni)
# biblioteca.prestar_libro(libro2, alumno1.dni)

# print(f"{alumno1.nombre} ha tomado prestado el libro {alumno1.libros_prestados}")