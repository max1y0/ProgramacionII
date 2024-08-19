class Fraccion:
	def __init__(self,num,denom):
		self.num = num
		self.denom = denom
	
	def show(self):
		return str(self.num) + " / " + str(self.denom)

	def por( self, fraccion2):
		resultado = Fraccion(1,1)
		resultado.num = self.num * fraccion2.num
		resultado.denom = self.denom * fraccion2.denom 
		return resultado

	def dividido( self, fraccion2):
		resultado = Fraccion(1,1)
		resultado.num = self.num * fraccion2.denom
		resultado.denom = self.denom * fraccion2.num 
		return resultado
	
	def mas( self, fraccion2):
		resultado = Fraccion(1,1)
		resultado.num = self.num * fraccion2.denom + self.denom * fraccion2.num 
		resultado.denom = self.denom * fraccion2.denom 
		return resultado

	def menos( self, fraccion2):
		resultado = Fraccion(1,1)
		resultado.num = self.num * fraccion2.denom - self.denom * fraccion2.num
		resultado.denom = self.denom * fraccion2.denom 
		return resultado

opcion = 1
while (opcion <5):
	print ("Ingrese una opcion: \n 1 - Sumar \n 2 - Restar \n 3 - Multiplicar \n 4 - Dividir \n")
	opcion = int(input())

	if (opcion ==1 ):
		fraccion1 = Fraccion(int(input("Ingrese la primer fraccion\n ")),int(input("--- \n ")))
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La suma es \n " + fraccion1.mas(fraccion2).show())

	if (opcion ==2 ):
		fraccion1 = Fraccion(int(input("Ingrese la primer fraccion\n ")),int(input("--- \n ")))
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La resta es \n " + fraccion1.menos(fraccion2).show())

	if (opcion ==3 ):
		fraccion1 = Fraccion(int(input("Ingrese la primer fraccion\n ")),int(input("--- \n ")))
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La multiplicación es \n " + fraccion1.por(fraccion2).show())

	if (opcion ==4 ):
		fraccion1 = Fraccion(int(input("Ingrese la primer fraccion\n ")),int(input("--- \n ")))
		fraccion2 = Fraccion(int(input("Ingrese la segunda fraccion\n ")),int(input("--- \n ")))
		print ("La división es \n " + fraccion1.dividido(fraccion2).show())
	input()





