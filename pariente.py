class Pariente ():
	def __init__ (self,nombre,app,parentezco):
		self.nombre = nombre
		self.app = app
		self.parentezco = parentezco

parientes = []
rta = "si"
while rta.lower() == "si":
	pariente1 = Pariente(
				input("pone su nombre"),
				input("pone su apellido"),
				input("pone tu parentezco")
				)
	parientes.append(pariente1)
	rta = input("quiere seguir cargando?")

opcion = 0
while opcion !=5:
	print("1- Mostrar Abuelos")
	print("2- Mostrar Padres")
	print("3- Mostrar Hermanos")
	print("4- Listar todos en orden ascendente")
	print("5- Salir")
	opcion = int(input())
	if opcion == 1:
		pass
		#acciones para mostrar los abuelos
	elif opcion ==2:
		pass
		#acciones para mostrar padres