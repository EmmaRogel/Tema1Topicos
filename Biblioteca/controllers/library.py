
from controllers import shelf, student
class Biblioteca:
    def __init__(self):
        self.estantes = {}
        self.alumnos = {}

    def agregar_estante(self, nombre):
        self.estantes[nombre] = shelf.Estante()

    def eliminar_estante(self, nombre):
        if nombre in self.estantes:
            del self.estantes[nombre]

    def agregar_libro_a_estante(self, libro, estante):
        if estante in self.estantes:
            self.estantes[estante].agregar_libro(libro)

    def eliminar_libro_de_estante(self, libro, estante):
        if estante in self.estantes:
            self.estantes[estante].eliminar_libro(libro)

    def obtener_inventario(self):
        inventario = {}
        for estante, libros in self.estantes.items():
            inventario[estante] = libros.obtener_inventario()
        return inventario

    def agregar_alumno(self, dni, nombre, apellido):
        self.alumnos[dni] = student.Alumno(nombre, apellido, dni)

    def eliminar_alumno(self, dni):
        if dni in self.alumnos:
            del self.alumnos[dni]

    def prestar_libro(self, libro, dni_alumno):
        if dni_alumno in self.alumnos :
                alumno = self.alumnos[dni_alumno]
                if libro not in alumno.libros_prestados:
                    alumno.libros_prestados.append(libro.titulo)
                    print(f"{alumno.nombre} ha tomado prestado el libro {libro.titulo}")
                else:
                    print(f"{alumno.nombre} ya tiene prestado el libro {libro.titulo}")