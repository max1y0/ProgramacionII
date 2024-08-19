class Fraccion:
	def __init__(self,num,denom):
		self.num = num
		self.denom = denom

	def mostrar(self):
		pass

	def por( self, fraccion2):
		pass

	def dividido( self, fraccion2):
		pass

	def mas( self, fraccion2):
		pass

	def menos( self, fraccion2):
		pass

opcion = 1

print ("Ingrese la primer fraccion\n")
fraccion1 = Fraccion(int(input()),int(input("--- \n ")))

while (opcion <5):
	print ("Ingrese una opcion: \n 1 - Sumar \n 2 - Restar \n 3 - Multiplicar \n 4 - Dividir \n")
	opcion = int(input())

	if (opcion ==1 ):
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La suma es \n " + fraccion1.mas(fraccion2).mostrar())

	if (opcion ==2 ):
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La resta es \n " + fraccion1.menos(fraccion2).mostrar())

	if (opcion ==3 ):
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La multiplicación es \n " + fraccion1.por(fraccion2).mostrar())

	if (opcion ==4 ):
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La división es \n " + fraccion1.dividido(fraccion2).mostrar())
	input()
