class Autor:
    def __init__(self, nombre, apellido, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad

    def mostrar_autor(self):
        return f"{self.nombre} {self.apellido} ({self.nacionalidad})"