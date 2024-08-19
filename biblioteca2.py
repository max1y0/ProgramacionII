class Libro:
	def __init__(self,titulo,autor,editorial,genero,año,disponibilidad):
		self.titulo = titulo
		self.autor = autor
		self.editorial = editorial
		self.genero = genero
		self.año = año
		self.disponibilidad = disponibilidad

	def prestar(self):
		self.disponibilidad = "no"

	def devolver(self):
		self.disponibilidad = "si"

	def imprimirInfo(self):
		print("Libro:", self.titulo)
		print("Autor:",self.autor)
		print("---------------------")
		print(self.editorial,self.año,self.genero)

biblioteca = []
opcion = 0
while opcion != 11:
	print("\n \n Bienvenido al sistema de gestión de biblioteca:")
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
	print("11. Salir")
	opcion = int(input("Ingrese el número de opción que desea ejecutar: "))

	if (opcion == 1):
		print("\n \n Sistema de carga de archivos")
		print(" -------------------------- ")
		libro = Libro (
			input("Ingrese el título "),
			input("Ingrese el autor "),
			input("Ingrese la editorial "),
			input("Ingrese el género "),
			input("Ingrese el año de publicación "),
			'si'
		)
		biblioteca.append(libro)
	elif (opcion == 2):
		pass
	elif (opcion == 3):
		pass
	elif (opcion == 4):
		pass
	elif (opcion == 5):
		pass
	elif (opcion == 6):
		for libro in biblioteca:
			libro.imprimirInfo()
	elif (opcion == 7):
		pass
	elif (opcion == 8):
		pass
	elif (opcion == 9):
		pass
	elif (opcion == 10):
		pass


