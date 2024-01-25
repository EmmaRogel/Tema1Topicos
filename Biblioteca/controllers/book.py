class Libro:
    def __init__(self, titulo, autor, ubicacion):
        self.titulo = titulo
        self.autor = autor
        self.ubicacion = ubicacion

    def __str__(self):
        return f"{self.titulo} - {self.autor.mostrar_autor()} - {self.ubicacion}"

