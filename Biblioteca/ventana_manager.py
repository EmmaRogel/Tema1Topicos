from views import ventana_home
from views import ventana_agregar_libros
from views import  agregar_libro_view
from views import ventana_agregar_alumno
from views import ventana_mostrar_alumnos
from views import  ventana_mostrar_prestamos
class VentanaManager:
    def __init__(self):
        self.ventana_principal =ventana_home.VentanaHome(self)
        self.nueva_ventana = None

    def iniciar_aplicacion(self):
        self.ventana_principal.iniciar_aplicacion()

        

    def abrir_nueva_ventana(self):
        self.nueva_ventana = ventana_agregar_libros.AgregarLibros(self)
        self.ventana_principal.ocultar_ventana()

    def abrir_mostrar_libro(self):
        self.mostrar_libros =agregar_libro_view.MostrarLibros(self)
        self.ventana_principal.ocultar_ventana()

    def abrir_agregar_alumno(self):
        self.agregar_alumno = ventana_agregar_alumno.AgregarAlumno(self)
        self.ventana_principal.ocultar_ventana()

    def abrir_mostrar_alumnos(self):
        self.mostrar_alumnos = ventana_mostrar_alumnos.MostrarAlumnos(self)
        self.ventana_principal.ocultar_ventana()

    def abrir_mostrar_prestamos(self):
        self.mostrar_prestamos = ventana_mostrar_prestamos.MostrarPrestamos(self)
        self.ventana_principal.ocultar_ventana()

    def mostrar_ventana_principal(self):
        self.ventana_principal.mostrar_ventana()
        if self.nueva_ventana:
            self.nueva_ventana = None

Lista_Prestamos=[]
if __name__ == "__main__":
    ventana_manager = VentanaManager()
    ventana_manager.iniciar_aplicacion()    