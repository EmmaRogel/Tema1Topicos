
from tkinter import messagebox

class Alumno:
    def __init__(self, nombre, apellido, dni, libros_prestados = []):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.libros_prestados = libros_prestados
   

    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni})"
    

    def ingresar_alumno(coleccion_alumnos, nombre, apellido, carrera, numero_control):
        if not nombre or not apellido or not carrera or not numero_control:
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
            return

        alumno = {
            "nombre": nombre,
            "apellido": apellido,
            "carrera": carrera,
            "numero_control": numero_control,
            "libros": [],
        }

        coleccion_alumnos.insert_one(alumno)
        messagebox.showinfo("Alumno ingresado", "Alumno ingresado con éxito.")
        return True 