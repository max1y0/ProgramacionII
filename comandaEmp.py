class ComandaEmp:
	def __init__(self,nombre,envio,tipo,
				cantidad,direccion, precio):
		self.nombre=nombre
		self.envio= envio
		self.tipo = tipo
		self.cantidad = cantidad
		self.direccion = direccion
		self.precio = precio

def ticket(com):
	print("********TICKET********")
	print("cliente:", com.nombre)
	print(com.cantidad, "empanadas de", com.tipo)
	print("direccion:", com.direccion)
	print("precio:", com.precio)

comanda1 = ComandaEmp (
	input("cual es su nombre"),
	input("envio? si/no"),
	input("que variedad?"),
	int(input("cuantas?")),
	input("direccion?"),
	int(input("Cuanto sale?"))
	)
comanda2 = ComandaEmp (
	input("cual es su nombre"),
	input("envio? si/no"),
	input("que variedad?"),
	int(input("cuantas?")),
	input("direccion?"),
	int(input("Cuanto sale?"))
	)
comanda3 = ComandaEmp (
	input("cual es su nombre"),
	input("envio? si/no"),
	input("que variedad?"),
	int(input("cuantas?")),
	input("direccion?"),
	int(input("Cuanto sale?")),
	)

ticket(comanda1)
ticket(comanda2)
ticket(comanda3)
