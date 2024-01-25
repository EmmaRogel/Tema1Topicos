import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bson import ObjectId
from pymongo import MongoClient
import ventana_manager


class MostrarAlumnos:
    def __init__(self, ventana_manager) -> None:

        self.ventana_manager = ventana_manager
        self.ventana_mostrar_alumnos = tk.Toplevel()
        self.ventana_mostrar_alumnos.title("Alumnos")

        # CONFIGURACIÓN PARA CENTRAR VENTANA
        screen_width = self.ventana_mostrar_alumnos.winfo_screenwidth()
        screen_height = self.ventana_mostrar_alumnos.winfo_screenheight()
        x_position = int((screen_width - 800) / 2)  
        y_position = int((screen_height - 600) / 2) 
        self.ventana_mostrar_alumnos.geometry(f"800x600+{x_position}+{y_position}")

         # CONFIGURACIONES PARA CENTRAR VENTANA
        for i in range(9):  
            self.ventana_mostrar_alumnos.grid_rowconfigure(i, weight=1)
        for i in range(4):  
            self.ventana_mostrar_alumnos.grid_columnconfigure(i, weight=1)

        # DEFINICIÓN DE LAS COLUMNAS PARA EL TREEVIEW
        columns = [
            "_id",
            "Nombre",
            "Apellido",
            "Carrera",
            "Número de Control",
            "Libros Prestados",
        ]

        # CREACIÓN DEL TREEVIEW CON LAS COLUMNAS DEFINIDAS
        self.tree = ttk.Treeview(
            self.ventana_mostrar_alumnos, columns=columns, show="headings"
        )

        # CONFIGURACIÓN DE ENCABEZADOS Y ANCLAJES PARA CADA COLUMNA
        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, width=100, minwidth=50, anchor=tk.CENTER)

        # AJUSTE DE ANCHO MAYOR PARA LA COLUMNA "LIBROS PRESTADOS"
        self.tree.column("Libros Prestados", width=200, minwidth=100, anchor=tk.CENTER)

        # POSICIONAMIENTO DEL TREEVIEW EN LA INTERFAZ GRÁFICA
        self.tree.grid(column=0, row=0, padx=20, pady=30, sticky="nsew", columnspan=4)

        # ENLACE DEL EVENTO DE CLIC PARA EJECUTAR LA FUNCIÓN "LLENAR_INPUTS" AL SOLTAR EL BOTÓN
        self.tree.bind("<ButtonRelease-1>", self.llenar_inputs)

        # CONEXIÓN A LA BASE DE DATOS MONGODB
        try:
            client = MongoClient(
                "mongodb+srv://bdata:1234@biblioteca.j9zcdza.mongodb.net/"
            )
            db = client["BibliotecaBigData"]
            self.coleccion_alumnos = db["Alumnos"]

            # LLAMADA A LA FUNCIÓN PARA CONSULTAR Y MOSTRAR ALUMNOS
            self.consultar_alumnos()
        except Exception as e:
            # MANEJO DE EXCEPCIONES EN CASO DE ERROR EN LA CONEXIÓN A LA BASE DE DATOS
            messagebox.showerror(
                "Error", f"Error al conectar a la base de datos: {str(e)}"
        )
        # VARIABLES DE CONTROL PARA LAS ENTRADAS RELACIONADAS CON LOS REGISTROS
        self.id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.carrera_var = tk.StringVar()
        self.numero_control_var = tk.StringVar()

        # ETIQUETAS E INPUTS PARA VISUALIZAR Y MODIFICAR DATOS DE ALUMNOS

        # ETIQUETA Y ENTRADA PARA EL CAMPO "ID"
        tk.Label(self.ventana_mostrar_alumnos, text="ID:").grid(
            row=1, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(
            self.ventana_mostrar_alumnos, textvariable=self.id_var, state="readonly", justify="center"
        ).grid(row=1, column=1, columnspan=3, sticky="w", padx=(0, 10))

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Nombre"
        tk.Label(self.ventana_mostrar_alumnos, text="Nombre:").grid(
            row=2, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(self.ventana_mostrar_alumnos, textvariable=self.nombre_var, justify="center").grid(
            row=2, column=1, columnspan=3, sticky="w", padx=(0, 10)
        )

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Apellido"
        tk.Label(self.ventana_mostrar_alumnos, text="Apellido:").grid(
            row=3, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(self.ventana_mostrar_alumnos, textvariable=self.apellido_var, justify="center").grid(
            row=3, column=1, columnspan=3, sticky="w", padx=(0, 10)
        )

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Carrera"
        tk.Label(self.ventana_mostrar_alumnos, text="Carrera:").grid(
            row=4, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(self.ventana_mostrar_alumnos, textvariable=self.carrera_var, justify="center").grid(
            row=4, column=1, columnspan=3, sticky="w", padx=(0, 10)
        )

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Número de Control"
        tk.Label(self.ventana_mostrar_alumnos, text="Número de Control:").grid(
            row=5, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(
            self.ventana_mostrar_alumnos, textvariable=self.numero_control_var, justify="center"
        ).grid(row=5, column=1, columnspan=3, sticky="w", padx=(0, 10))

        # BOTONES DE ACCIÓN PARA MODIFICAR, INSERTAR, ELIMINAR, LIMPIAR Y REGRESAR

        # BOTÓN PARA MODIFICAR ALUMNO
        tk.Button(
            self.ventana_mostrar_alumnos,
            text="Modificar alumno",
            command=self.modificar_alumno,
        ).grid(row=1, column=2)

        # BOTÓN PARA INSERTAR ALUMNO
        tk.Button(
            self.ventana_mostrar_alumnos,
            text="Insertar alumno",
            command=self.ingresar_alumno,
        ).grid(row=2, column=2)

        # BOTÓN PARA ELIMINAR ALUMNO
        tk.Button(
            self.ventana_mostrar_alumnos,
            text="Eliminar alumno",
            command=self.eliminar_alumno,
        ).grid(row=3, column=2)

        # BOTÓN PARA LIMPIAR LOS CAMPOS DE ENTRADA
        tk.Button(
            self.ventana_mostrar_alumnos, text="Limpiar", command=self.limpiar_inputs
        ).grid(row=4, column=2)

        # BOTÓN PARA REGRESAR A LA VENTANA PRINCIPAL
        tk.Button(
            self.ventana_mostrar_alumnos,
            text="Regresar",
            command=self.cerrar_y_mostrar_principal,
        ).grid(row=5, column=2)


    # MÉTODO PARA LLENAR LAS ENTRADAS CON LOS DATOS SELECCIONADOS EN EL TREEVIEW
    def llenar_inputs(self, event):
        # OBTENER EL ÍTEM SELECCIONADO EN EL TREEVIEW
        item = self.tree.selection()
        # VERIFICAR SI SE HA SELECCIONADO AL MENOS UN ÍTEM
        if item:
            # TOMAR SOLO EL PRIMER ELEMENTO SI HAY SELECCIONES MÚLTIPLES
            item = item[0]
            # OBTENER LOS VALORES DEL ÍTEM SELECCIONADO EN EL TREEVIEW
            values = self.tree.item(item, "values")
            # ASIGNAR LOS VALORES A LAS VARIABLES DE CONTROL DE LAS ENTRADAS
            self.id_var.set(values[0])
            self.nombre_var.set(values[1])
            self.apellido_var.set(values[2])
            self.carrera_var.set(values[3])
            self.numero_control_var.set(values[4])

    def cerrar_y_mostrar_principal(self):
        self.ventana_mostrar_alumnos.destroy()
        self.ventana_manager.mostrar_ventana_principal()

    # MÉTODO PARA CONSULTAR Y MOSTRAR LOS ALUMNOS EN EL TREEVIEW
    def consultar_alumnos(self):
        # LIMPIAR LA TABLA EN EL TREEVIEW
        self.tree.delete(*self.tree.get_children())
        # OBTENER LA LISTA DE ALUMNOS DESDE LA BASE DE DATOS
        lista_alumnos = list(self.coleccion_alumnos.find())
        # VERIFICAR SI NO HAY ALUMNOS REGISTRADOS
        if not lista_alumnos:
            # MOSTRAR UNA VENTANA DE INFORMACIÓN EN CASO DE NO HABER ALUMNOS
            messagebox.showinfo(
                "Información", "No hay alumnos registrados en el sistema."
            )
            return
        # ITERAR SOBRE LA LISTA DE ALUMNOS Y LLENAR EL TREEVIEW CON LOS DATOS
        for alumno in lista_alumnos:
            # OBTENER LOS DATOS DE CADA ALUMNO
            id = alumno.get("_id", "")
            nombre = alumno.get("nombre", "")
            apellido = alumno.get("apellido", "")
            numero_control = alumno.get("numero_control", "")
            carrera = alumno.get("carrera", "")
            libros_prestados = alumno.get("libros", [])
            # CREAR UNA CADENA CON LOS NOMBRES DE LOS LIBROS PRESTADOS
            libros_str = ", ".join(
                [libro.get("nombre", "Libro Desconocido") for libro in libros_prestados]
            )
            # INSERTAR UN NUEVO ÍTEM EN EL TREEVIEW CON LOS DATOS DEL ALUMNO
            self.tree.insert(
                "",
                "end",
                values=(id, nombre, apellido, carrera, numero_control, libros_str),
            )

    # MÉTODO PARA MODIFICAR LOS DATOS DE UN ALUMNO
    def modificar_alumno(self):
        # OBTENER LOS NUEVOS VALORES DE LOS CAMPOS DE ENTRADA
        nuevo_nombre = self.nombre_var.get()
        nuevo_apellido = self.apellido_var.get()
        nueva_carrera = self.carrera_var.get()
        nuevo_numero_control = self.numero_control_var.get()
        # VALIDAR QUE NO HAYA CAMPOS VACÍOS
        if (
            not nuevo_nombre
            or not nuevo_apellido
            or not nueva_carrera
            or not nuevo_numero_control
        ):
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI HAY CAMPOS VACÍOS
            messagebox.showwarning(
                "Campos vacíos", "Por favor, complete todos los campos."
            )
            return
        # VALIDAR QUE EL NÚMERO DE CONTROL TENGA 8 DÍGITOS
        if not (len(nuevo_numero_control) == 8):
            messagebox.showwarning(
                "Número de Control inválido",
                "El número de control debe tener 8 dígitos.",
            )
            return
        # OBTENER EL ID DEL ALUMNO COMO UN STRING
        id_alumno_str = self.id_var.get()
        # CONVERTIR EL ID A ObjectId
        id_alumno = ObjectId(id_alumno_str)
        # MOSTRAR UN MENSAJE DE CONFIRMACIÓN ANTES DE REALIZAR LA MODIFICACIÓN
        confirmacion = messagebox.askyesno(
            "Confirmar modificación", "¿Está seguro de que desea modificar el alumno?"
        )
        if confirmacion:
            # OBTENER EL ALUMNO DE LA BASE DE DATOS
            alumno = self.coleccion_alumnos.find_one({"_id": id_alumno})
            # VERIFICAR SI EXISTE UN ALUMNO CON ESE ID
            if not alumno:
                messagebox.showwarning(
                    "Alumno no encontrado", "No existe un alumno con ese ID."
                )
                return
            # VALIDAR SI HAY MODIFICACIONES ANTES DE ACTUALIZAR
            if (
                nuevo_nombre == alumno["nombre"]
                and nuevo_apellido == alumno["apellido"]
                and nueva_carrera == alumno["carrera"]
                and nuevo_numero_control == alumno["numero_control"]
            ):
                # MOSTRAR UN MENSAJE SI NO HAY CAMBIOS REALIZADOS
                messagebox.showinfo(
                    "Sin modificaciones", "No se realizaron cambios en el alumno."
                )
                return
            # ACTUALIZAR LOS DATOS DEL ALUMNO EN LA BASE DE DATOS
            resultado = self.coleccion_alumnos.update_one(
                {"_id": id_alumno},
                {
                    "$set": {
                        "nombre": nuevo_nombre,
                        "apellido": nuevo_apellido,
                        "carrera": nueva_carrera,
                        "numero_control": nuevo_numero_control,
                    }
                },
            )
            # VERIFICAR SI SE REALIZÓ LA ACTUALIZACIÓN
            if resultado.modified_count == 1:
                messagebox.showinfo(
                    "Alumno actualizado", "Alumno actualizado con éxito."
                )
            else:
                messagebox.showinfo(
                    "Sin modificaciones", "No se realizaron cambios en el alumno."
                )
            # LIMPIAR LOS CAMPOS DESPUÉS DE MODIFICAR EL ALUMNO
            self.limpiar_inputs()
            # ACTUALIZAR LA TABLA DE ALUMNOS EN EL TREEVIEW
            self.consultar_alumnos()

    # MÉTODO PARA ELIMINAR UN ALUMNO
    def eliminar_alumno(self):
        # OBTENER EL ID DEL ALUMNO COMO UN STRING
        id_alumno_str = self.id_var.get()
        # VALIDAR QUE NO HAYA CAMPOS VACÍOS
        if not id_alumno_str:
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI NO SE HA SELECCIONADO UN ALUMNO
            messagebox.showwarning(
                "Campo vacío", "Por favor, seleccione un alumno para eliminar."
            )
            return
        # CONVERTIR EL ID A ObjectId
        id_alumno = ObjectId(id_alumno_str)
        # MOSTRAR UN MENSAJE DE CONFIRMACIÓN ANTES DE REALIZAR LA ELIMINACIÓN
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación", "¿Está seguro de que desea eliminar el alumno?"
        )
        if confirmacion:
            # OBTENER EL ALUMNO DE LA BASE DE DATOS
            alumno = self.coleccion_alumnos.find_one({"_id": id_alumno})
            # VERIFICAR SI EXISTE UN ALUMNO CON ESE ID
            if not alumno:
                messagebox.showwarning(
                    "Alumno no encontrado", "No existe un alumno con ese ID."
                )
                return
            # OBTENER LA LISTA DE LIBROS PRESTADOS POR EL ALUMNO
            libros_prestados = alumno.get("libros", [])
            # VERIFICAR SI EL ALUMNO TIENE LIBROS PRESTADOS
            if libros_prestados:
                # MOSTRAR UN MENSAJE INFORMATIVO SI EL ALUMNO TIENE LIBROS PRESTADOS
                messagebox.showinfo(
                    "Libros prestados",
                    "El alumno tiene libros prestados. Devuélvalos antes de eliminar al alumno.",
                )
                return
            # REALIZAR LA ELIMINACIÓN DEL ALUMNO
            resultado = self.coleccion_alumnos.delete_one({"_id": id_alumno})
            # VERIFICAR SI SE REALIZÓ LA ELIMINACIÓN
            if resultado.deleted_count == 1:
                messagebox.showinfo("Alumno eliminado", "Alumno eliminado con éxito.")
            else:
                messagebox.showinfo(
                    "Sin eliminación", "No se realizó la eliminación del alumno."
                )
            # LIMPIAR LOS CAMPOS DESPUÉS DE ELIMINAR EL ALUMNO
            self.limpiar_inputs()
            # ACTUALIZAR LA TABLA DE ALUMNOS EN EL TREEVIEW
            self.consultar_alumnos()

    def limpiar_inputs(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.carrera_var.set("")
        self.numero_control_var.set("")

    # MÉTODO PARA INGRESAR UN NUEVO ALUMNO
    def ingresar_alumno(self):
        # OBTENER LOS VALORES DE LAS VARIABLES DE CONTROL DE LAS ENTRADAS
        nombre_alumno = self.nombre_var.get()
        apellido_alumno = self.apellido_var.get()
        carrera_alumno = self.carrera_var.get()
        numero_control_alumno = self.numero_control_var.get()
        # VERIFICAR SI ALGÚN CAMPO ESTÁ VACÍO
        if (
            not nombre_alumno
            or not apellido_alumno
            or not carrera_alumno
            or not numero_control_alumno
        ):
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI HAY CAMPOS VACÍOS
            messagebox.showwarning(
                "Campos vacíos", "Por favor, complete todos los campos."
            )
            return
        # VERIFICAR QUE EL NÚMERO DE CONTROL SEA UN NÚMERO DE 8 DÍGITOS
        if len(numero_control_alumno) < 8 or len(numero_control_alumno) > 8:
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI EL NÚMERO DE CONTROL NO TIENE 8 DÍGITOS
            messagebox.showwarning(
                "Formato incorrecto",
                "El campo 'Número de Control' debe tener 8 dígitos.",
            )
            return
        # VERIFICAR SI EL NÚMERO DE CONTROL YA EXISTE EN LA BASE DE DATOS
        if self.coleccion_alumnos.find_one({"numero_control": numero_control_alumno}):
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI YA EXISTE UN ALUMNO CON EL MISMO NÚMERO DE CONTROL
            messagebox.showwarning(
                "Registro existente",
                "Ya existe un alumno con este número de control en la base de datos.",
            )
            return
        # CREAR UN DICCIONARIO CON LOS DATOS DEL ALUMNO
        alumno = {
            "nombre": nombre_alumno,
            "apellido": apellido_alumno,
            "carrera": carrera_alumno,
            "numero_control": numero_control_alumno,
            "libros": [],
        }
        try:
            # INSERTAR EL ALUMNO EN LA BASE DE DATOS
            self.coleccion_alumnos.insert_one(alumno)
            # MOSTRAR UN MENSAJE DE INFORMACIÓN SI SE INGRESÓ EL ALUMNO EXITOSAMENTE
            messagebox.showinfo("Alumno ingresado", "Alumno ingresado con éxito.")
            # LIMPIAR LOS CAMPOS DE ENTRADA
            self.limpiar_inputs()
            # ACTUALIZAR LA TABLA DE ALUMNOS EN EL TREEVIEW
            self.consultar_alumnos()
        except Exception as e:
            # MOSTRAR UN MENSAJE DE ERROR SI OCURRE UN PROBLEMA AL INGRESAR EL ALUMNO
            messagebox.showerror("Error", f"Error al ingresar el alumno: {str(e)}")

if __name__ == "__main__":
    ventana_manager = ventana_manager.VentanaManager()
    ventana_mostrar_alumnos = MostrarAlumnos(ventana_manager)
    ventana_mostrar_alumnos.ventana_mostrar_alumnos.mainloop()
