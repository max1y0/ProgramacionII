class Libro:
    def __init__(self, titulo, autor, editorial, genero, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.genero = genero
        self.anio_publicacion = anio_publicacion
        self.disponibilidad = True

    def imprimirInformacion(self):
        print("Título:", self.titulo)
        print("Autor:", self.autor)
        print("Editorial:", self.editorial)
        print("Género:", self.genero)
        print("Año de publicación:", self.anio_publicacion)
        print("Disponibilidad:", "Disponible" if self.disponibilidad else "No disponible")

    def prestamo(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print("Libro prestado exitosamente.")
        else:
            print("Error: El libro ya ha sido prestado.")

    def devolucion(self):
        if not self.disponibilidad:
            self.disponibilidad = True
            print("Libro devuelto exitosamente.")
        else:
            print("Error: El libro ya ha sido devuelto.")

    def antiguedad(self, anio_actual):
        antiguedad = anio_actual - self.anio_publicacion
        return antiguedad


def cargar_libro(lista_libros):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    genero = input("Ingrese el género del libro: ")
    anio_publicacion = int(input("Ingrese el año de publicación del libro: "))

    for libro in lista_libros:
        if libro.titulo == titulo:
            print("Error: El libro ya está cargado.")
            return

    libro = Libro(titulo, autor, editorial, genero, anio_publicacion)
    lista_libros.append(libro)
    print("Libro cargado exitosamente.")


def modificar_libro(lista_libros):
    titulo = input("Ingrese el título del libro que desea modificar: ")

    for libro in lista_libros:
        if libro.titulo == titulo:
            autor = input("Ingrese el nuevo autor del libro: ")
            editorial = input("Ingrese la nueva editorial del libro: ")
            genero = input("Ingrese el nuevo género del libro: ")
            anio_publicacion = int(input("Ingrese el nuevo año de publicación del libro: "))

            libro.autor = autor
            libro.editorial = editorial
            libro.genero = genero
            libro.anio_publicacion = anio_publicacion
            print("Libro modificado exitosamente.")
            return

    print("Error: Libro no encontrado.")


def eliminar_libro(lista_libros):
    titulo = input("Ingrese el título del libro que desea eliminar: ")

    for libro in lista_libros:
        if libro.titulo == titulo:
            lista_libros.remove(libro)
            print("Libro eliminado exitosamente.")
            return

    print("Error: Libro no encontrado.")


def prestar_libro(lista_libros):
    titulo = input("Ingrese el título del libro que desea prestar: ")

    for libro in lista_libros:
        if libro.titulo == titulo:
            libro.prestamo()
            return

    print("Error: Libro no encontrado.")


def devolver_libro(lista_libros):
    titulo = input("Ingrese el título del libro que desea devolver: ")

    for libro in lista_libros:
        if libro.titulo == titulo:
            libro.devolucion()
            return

    print("Error: Libro no encontrado.")


def listar_libros(lista_libros):
    print("Listado de libros:")
    for libro in lista_libros:
        libro.imprimirInformacion()
        print("------------------------")


def listar_libros_prestados(lista_libros):
    print("Listado de libros prestados:")
    libros_prestados = [libro for libro in lista_libros if not libro.disponibilidad]

    if libros_prestados:
        for libro in libros_prestados:
            libro.imprimirInformacion()
            print("------------------------")
    else:
        print("No existen libros prestados.")


def listar_libros_disponibles(lista_libros):
    print("Listado de libros disponibles:")
    libros_disponibles = [libro for libro in lista_libros if libro.disponibilidad]

    if libros_disponibles:
        for libro in libros_disponibles:
            libro.imprimirInformacion()
            print("------------------------")
    else:
        print("No existen libros disponibles.")


def listar_libros_por_genero(lista_libros):
    genero = input("Ingrese el género de los libros que desea listar: ")
    libros_genero = [libro for libro in lista_libros if libro.genero == genero]

    if libros_genero:
        print(f"Listado de libros del género '{genero}':")
        for libro in libros_genero:
            libro.imprimirInformacion()
            print("------------------------")
    else:
        print(f"No existen libros en el género '{genero}'.")


def listar_libros_modernos(lista_libros, anio_actual):
    print("Listado de libros modernos:")
    libros_modernos = [libro for libro in lista_libros if libro.antiguedad(anio_actual) < 20]

    if libros_modernos:
        for libro in libros_modernos:
            libro.imprimirInformacion()
            print("------------------------")
    else:
        print("No existen libros modernos.")

def mostrar_menu():
    print("Bienvenido al sistema de gestión de biblioteca:")
    print("1. Cargar un libro")
    print("2. Modificar un libro")
    print("3. Eliminar un libro")
    print("4. Prestar un libro")
    print("5. Devolver un libro")
    print("6. Listar todos los libros")
    print("7. Listar libros prestados")
    print("8. Listar libros disponibles")
    print("9. Listar libros por género")
    print("10. Listar libros modernos")
    print("0. Salir")


def ejecutar_sistema():
    lista_libros = []
    anio_actual = 2023

    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción que desea ejecutar: ")

        if opcion == "1":
            cargar_libro(lista_libros)
        elif opcion == "2":
            modificar_libro(lista_libros)
        elif opcion == "3":
            eliminar_libro(lista_libros)
        elif opcion == "4":
            prestar_libro(lista_libros)
        elif opcion == "5":
            devolver_libro(lista_libros)
        elif opcion == "6":
            listar_libros(lista_libros)
        elif opcion == "7":
            listar_libros_prestados(lista_libros)
        elif opcion == "8":
            listar_libros_disponibles(lista_libros)
        elif opcion == "9":
            listar_libros_por_genero(lista_libros)
        elif opcion == "10":
            listar_libros_modernos(lista_libros, anio_actual)
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")


ejecutar_sistema()
