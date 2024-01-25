import tkinter as tk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from bson import ObjectId
from pymongo import MongoClient
import ventana_manager

class MostrarLibros:
    def __init__(self, ventana_manager):
        self.ventana_manager = ventana_manager
        self.ventana_mostrar_libros = tk.Toplevel()
        self.ventana_mostrar_libros.title("Libros")
        
        # CONFIGURACIÓN PARA CENTRAR VENTANA
        screen_width = self.ventana_mostrar_libros.winfo_screenwidth()
        screen_height = self.ventana_mostrar_libros.winfo_screenheight()
        x_position = int((screen_width - 800) / 2)  
        y_position = int((screen_height - 600) / 2)  
        self.ventana_mostrar_libros.geometry(f"800x600+{x_position}+{y_position}")

         # CONFIGURACIONES PARA CENTRAR VENTANA
        for i in range(9):  
            self.ventana_mostrar_libros.grid_rowconfigure(i, weight=1)
        for i in range(4):  
            self.ventana_mostrar_libros.grid_columnconfigure(i, weight=1)

        # DEFINICIÓN DE LAS COLUMNAS PARA EL TREEVIEW
        columns = [
            "_id",
            "Nombre Libro",
            "Categoía",
            "Nombre Autor",
            "Apellido Autor",
            "Nacionalidad Autor",
        ]

        # CREACIÓN DEL TREEVIEW CON LAS COLUMNAS DEFINIDAS
        self.tree = ttk.Treeview(
            self.ventana_mostrar_libros, columns=columns, show="headings"
        )

        # CONFIGURACIÓN DE ENCABEZADOS Y ANCLAJES PARA CADA COLUMNA
        for col in columns:
            self.tree.heading(col, text=col, anchor=tk.CENTER)
            self.tree.column(col, width=100, minwidth=50, anchor=tk.CENTER)

        # AJUSTE DE ANCHO MAYOR PARA LA COLUMNA "NOMBRE LIBRO"
        self.tree.column("Nombre Libro", width=215, minwidth=100, anchor=tk.CENTER)

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
            self.coleccion_libros = db["Libros"]

            # LLAMADA A LA FUNCIÓN PARA CONSULTAR Y MOSTRAR LIBROS
            self.consultar_libros()
        except Exception as e:
            # MANEJO DE EXCEPCIONES EN CASO DE ERROR EN LA CONEXIÓN A LA BASE DE DATOS
            messagebox.showerror(
                "Error", f"Error al conectar a la base de datos: {str(e)}"
        )

        # VARIABLES DE CONTROL PARA LAS ENTRADAS RELACIONADAS CON LOS REGISTROS
        self.id_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.nomautor_var = tk.StringVar()
        self.apeautor_var = tk.StringVar()
        self.nacautor_var = tk.StringVar()

        # ETIQUETAS E INPUTS PARA VISUALIZAR Y MODIFICAR DATOS DE LIBROS

        # ETIQUETA Y ENTRADA PARA EL CAMPO "ID"
        tk.Label(self.ventana_mostrar_libros, text="ID:").grid(
            row=1, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(
            self.ventana_mostrar_libros, textvariable=self.id_var, state="readonly", justify="center"
        ).grid(row=1, column=1, columnspan=3, sticky="w", padx=(0, 10))

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Nombre"
        tk.Label(self.ventana_mostrar_libros, text="Nombre:").grid(
            row=2, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(self.ventana_mostrar_libros, textvariable=self.nombre_var, justify="center").grid(
            row=2, column=1, columnspan=3, sticky="w", padx=(0, 10)
        )

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Categoría"
        tk.Label(self.ventana_mostrar_libros, text="Categoría:").grid(
            row=3, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(self.ventana_mostrar_libros, textvariable=self.categoria_var, justify="center").grid(
            row=3, column=1, columnspan=3, sticky="w", padx=(0, 10)
        )

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Nombre Autor"
        tk.Label(self.ventana_mostrar_libros, text="Nombre Autor:").grid(
            row=4, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(self.ventana_mostrar_libros, textvariable=self.nomautor_var, justify="center").grid(
            row=4, column=1, columnspan=3, sticky="w", padx=(0, 10)
        )

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Apellido Autor"
        tk.Label(self.ventana_mostrar_libros, text="Apellido Autor:").grid(
            row=5, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(
            self.ventana_mostrar_libros, textvariable=self.apeautor_var, justify="center"
        ).grid(row=5, column=1, columnspan=3, sticky="w", padx=(0, 10))

        # ETIQUETA Y ENTRADA PARA EL CAMPO "Nacionalidad Autor"
        tk.Label(self.ventana_mostrar_libros, text="Nacionalidad Autor:").grid(
            row=6, column=0, sticky="e", padx=(10, 0)
        )
        tk.Entry(
            self.ventana_mostrar_libros, textvariable=self.nacautor_var, justify="center"
        ).grid(row=6, column=1, columnspan=3, sticky="w", padx=(0, 10))

        # BOTONES DE ACCIÓN PARA MODIFICAR, INSERTAR, ELIMINAR, LIMPIAR Y REGRESAR

        # BOTÓN PARA MODIFICAR LIBRO
        tk.Button(
            self.ventana_mostrar_libros,
            text="Modificar Libro",
            command=self.modificar_libro,
        ).grid(row=1, column=2)

        # BOTÓN PARA INSERTAR LIBRO
        tk.Button(
            self.ventana_mostrar_libros,
            text="Insertar Libro",
            command=self.ingresar_libro,
        ).grid(row=2, column=2)

        # BOTÓN PARA ELIMINAR LIBRO
        tk.Button(
            self.ventana_mostrar_libros,
            text="Eliminar Libro",
            command=self.eliminar_libro,
        ).grid(row=3, column=2)

        # BOTÓN PARA LIMPIAR LOS CAMPOS DE ENTRADA
        tk.Button(
            self.ventana_mostrar_libros, text="Limpiar", command=self.limpiar_inputs
        ).grid(row=4, column=2)

        # BOTÓN PARA REGRESAR A LA VENTANA PRINCIPAL
        tk.Button(
            self.ventana_mostrar_libros,
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
            self.categoria_var.set(values[2])
            self.nomautor_var.set(values[3])
            self.apeautor_var.set(values[4])
            self.nacautor_var.set(values[5])

    def cerrar_y_mostrar_principal(self):
        self.ventana_mostrar_libros.destroy()
        self.ventana_manager.mostrar_ventana_principal()

    # MÉTODO PARA CONSULTAR Y MOSTRAR LOS LIBROS EN EL TREEVIEW
    def consultar_libros(self):
        # LIMPIAR LA TABLA EN EL TREEVIEW
        self.tree.delete(*self.tree.get_children())
        # OBTENER LA LISTA DE LIBROS DESDE LA BASE DE DATOS
        lista_libros = list(self.coleccion_libros.find())
        # VERIFICAR SI NO HAY LIBROS REGISTRADOS
        if not lista_libros:
            # MOSTRAR UNA VENTANA DE INFORMACIÓN EN CASO DE NO HABER LIBROS
            messagebox.showinfo(
                "Información", "No hay libros registrados en el sistema."
            )
            return
        # ITERAR SOBRE LA LISTA DE LIBROS Y LLENAR EL TREEVIEW CON LOS DATOS
        for libro in lista_libros:
            # OBTENER LOS DATOS DE CADA LIBRO
            id = libro.get("_id", "")
            nombre = libro.get("nombre", "")
            categoria = libro.get("categoria", "")
            nombre_autor = libro.get("autor.nombre", "")
            apellido_autor = libro.get("autor.apellido", "")
            nacionalidad_autor = libro.get("autor.nacionalidad", [])
            # INSERTAR UN NUEVO ÍTEM EN EL TREEVIEW CON LOS DATOS DEL LIBRO
            self.tree.insert(
                "",
                "end",
                values=(id, nombre, categoria, nombre_autor, apellido_autor, nacionalidad_autor),
            )

    # MÉTODO PARA MODIFICAR LOS DATOS DE UN LIBRO
    def modificar_libro(self):
        # OBTENER LOS NUEVOS VALORES DE LOS CAMPOS DE ENTRADA
        nuevo_nombre = self.nombre_var.get()
        nueva_categoria = self.categoria_var.get()
        nuevo_nomaoautor = self.nomautor_var.get()
        nuevo_apeautor = self.apeautor_var.get()
        nueva_nacautor = self.nacautor_var.get()
        # VALIDAR QUE NO HAYA CAMPOS VACÍOS
        if (
            not nuevo_nombre
            or not nueva_categoria
            or not nuevo_nomaoautor
            or not nuevo_apeautor
            or not nueva_nacautor
        ):
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI HAY CAMPOS VACÍOS
            messagebox.showwarning(
                "Campos vacíos", "Por favor, complete todos los campos."
            )
            return
        # OBTENER EL ID DEL LIBRO COMO UN STRING
        id_libro_str = self.id_var.get()
        # CONVERTIR EL ID A ObjectId
        id_libro = ObjectId(id_libro_str)
        # MOSTRAR UN MENSAJE DE CONFIRMACIÓN ANTES DE REALIZAR LA MODIFICACIÓN
        confirmacion = messagebox.askyesno(
            "Confirmar modificación", "¿Está seguro de que desea modificar el libro?"
        )
        if confirmacion:
            # OBTENER EL LIBRO DE LA BASE DE DATOS
            libro = self.coleccion_libros.find_one({"_id": id_libro})
            # VERIFICAR SI EXISTE UN LIBRO CON ESE ID
            if not libro:
                messagebox.showwarning(
                    "Libro no encontrado", "No existe un libro con ese ID."
                )
                return
            # VALIDAR SI HAY MODIFICACIONES ANTES DE ACTUALIZAR
            if (
                nuevo_nombre == libro["nombre"]
                and nueva_categoria == libro["categoria"]
                and nuevo_nomaoautor == libro["autor.nombre"]
                and nuevo_apeautor == libro["autor.apellido"]
                and nueva_nacautor == libro["autor.nacionalidad"]
            ):
                # MOSTRAR UN MENSAJE SI NO HAY CAMBIOS REALIZADOS
                messagebox.showinfo(
                    "Sin modificaciones", "No se realizaron cambios en el libro."
                )
                return
            # ACTUALIZAR LOS DATOS DEL LIBRO EN LA BASE DE DATOS
            resultado = self.coleccion_libros.update_one(
                {"_id": id_libro},
                {
                    "$set": {
                        "nombre": nuevo_nombre,
                        "categoria": nueva_categoria,
                        "autor.nombre": nuevo_nomaoautor,
                        "autor.apellido": nuevo_apeautor,
                        "autor.nacionalidad": nueva_nacautor,
                    }
                },
            )
            # VERIFICAR SI SE REALIZÓ LA ACTUALIZACIÓN
            if resultado.modified_count == 1:
                messagebox.showinfo(
                    "Libro actualizado", "Libro actualizado con éxito."
                )
            else:
                messagebox.showinfo(
                    "Sin modificaciones", "No se realizaron cambios en el Libro."
                )
            # LIMPIAR LOS CAMPOS DESPUÉS DE MODIFICAR EL LIBRO
            self.limpiar_inputs()
            # ACTUALIZAR LA TABLA DE LIRBOS EN EL TREEVIEW
            self.consultar_libros()

    # MÉTODO PARA ELIMINAR UN LIBRO
    def eliminar_libro(self):
        # OBTENER EL ID DEL LIBRO COMO UN STRING
        id_libro_str = self.id_var.get()
        # VALIDAR QUE NO HAYA CAMPOS VACÍOS
        if not id_libro_str:
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI NO SE HA SELECCIONADO UN LIBRO
            messagebox.showwarning(
                "Campo vacío", "Por favor, seleccione un libro para eliminar."
            )
            return
        # CONVERTIR EL ID A ObjectId
        id_libro = ObjectId(id_libro_str)
        # MOSTRAR UN MENSAJE DE CONFIRMACIÓN ANTES DE REALIZAR LA ELIMINACIÓN
        confirmacion = messagebox.askyesno(
            "Confirmar eliminación", "¿Está seguro de que desea eliminar el libro?"
        )
        if confirmacion:
            # OBTENER EL LIBRO DE LA BASE DE DATOS
            libro = self.coleccion_libros.find_one({"_id": id_libro})
            # VERIFICAR SI EXISTE UN LIBRO CON ESE ID
            if not libro:
                messagebox.showwarning(
                    "Libro no encontrado", "No existe un libro con ese ID."
                )
                return
            # REALIZAR LA ELIMINACIÓN DEL LIBRO
            resultado = self.coleccion_libros.delete_one({"_id": id_libro})
            # VERIFICAR SI SE REALIZÓ LA ELIMINACIÓN
            if resultado.deleted_count == 1:
                messagebox.showinfo("Libro eliminado", "Libro eliminado con éxito.")
            else:
                messagebox.showinfo(
                    "Sin eliminación", "No se realizó la eliminación del libro."
                )
            # LIMPIAR LOS CAMPOS DESPUÉS DE ELIMINAR EL LIBRO
            self.limpiar_inputs()
            # ACTUALIZAR LA TABLA DE LIBROS EN EL TREEVIEW
            self.consultar_libros()

    def limpiar_inputs(self):
        self.id_var.set("")
        self.nombre_var.set("")
        self.apellido_var.set("")
        self.carrera_var.set("")
        self.numero_control_var.set("")

    # MÉTODO PARA INGRESAR UN NUEVO LIBRO
    def ingresar_libro(self):
        # OBTENER LOS VALORES DE LAS VARIABLES DE CONTROL DE LAS ENTRADAS
        nombre = self.nombre_var.get()
        categoria = self.categoria_var.get()
        nombre_autor = self.nomautor_var.get()
        apellido_autor = self.apeautor_var.get()
        nacionalidad_autor = self.nacautor_var.get()
        # VERIFICAR SI ALGÚN CAMPO ESTÁ VACÍO
        if (
            not nombre
            or not categoria
            or not nombre_autor
            or not apellido_autor
            or not nacionalidad_autor
        ):
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI HAY CAMPOS VACÍOS
            messagebox.showwarning(
                "Campos vacíos", "Por favor, complete todos los campos."
            )
            return
        # VERIFICAR SI EL NOMBRE YA EXISTE EN LA BASE DE DATOS
        if self.coleccion_libros.find_one({"nombre": nombre}):
            # MOSTRAR UN MENSAJE DE ADVERTENCIA SI YA EXISTE UN LIBRO CON EL MISMO NOMBRE
            messagebox.showwarning(
                "Registro existente",
                "Ya existe un libro con este nombre en la base de datos.",
            )
            return
        # CREAR UN DICCIONARIO CON LOS DATOS DEL LIBRO
        libro = {
            "nombre": nombre,
            "categoria": categoria,
            "autor.nombre": nombre_autor,
            "autor.apellido": apellido_autor,
            "autor.nacionalidad": nacionalidad_autor
        }
        try:
            # INSERTAR EL LIBRO EN LA BASE DE DATOS
            self.coleccion_libros.insert_one(libro)
            # MOSTRAR UN MENSAJE DE INFORMACIÓN SI SE INGRESÓ EL LIBRO EXITOSAMENTE
            messagebox.showinfo("Libro ingresado", "Libro ingresado con éxito.")
            # LIMPIAR LOS CAMPOS DE ENTRADA
            self.limpiar_inputs()
            # ACTUALIZAR LA TABLA DE LIBROS EN EL TREEVIEW
            self.consultar_libros()
        except Exception as e:
            # MOSTRAR UN MENSAJE DE ERROR SI OCURRE UN PROBLEMA AL INGRESAR EL LIBRO
            messagebox.showerror("Error", f"Error al ingresar el libro: {str(e)}")
