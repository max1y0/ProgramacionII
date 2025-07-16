class Uno:
    def __init__(self,numero,color):
        self.numero = numero
        self.color = color

mazo = Uno(random.randint(0,9) , random.choice(['rojo','azul','verde','amarillo']) )

num = int(input())
col = input()

carta = Uno(num,col)

def puedoJugar (mazo,carta):
    if (mazo.numero == carta.numero or mazo.color == carta.color):
        return True
    else:
        return False

print (puedoJugar(mazo,carta))

#---------------
import random

class Uno:
    def __init__(self,color,numero):
        self.color = color
        self.numero = numero
# Pedir por usuario un número y un color

# Crear un objeto 'carta' que tenga el número y el color ingresados anteriormente

# hacer un print con la carta ingresada


#-----------
# ----------------- #
import random

class Uno:
    def __init__(self,numero,color):
        self.color = color
        self.numero = numero

num = int(input())
col = input()

carta = Uno(num,col)

print("------CARTA------")
print(carta.numero, "**************")
print("*************",carta.color )

# Código para crear una carta al azar, llamada "mazo" NO MODIFICAR
mazo = Uno( random.randint(0,9) , random.choice(['rojo','azul','verde','amarillo']) )
print("------MAZO------")
print(mazo.numero, "**************")
print("*************",mazo.color )

# Hacer una función que detecte si puedo jugar la carta en el mazo.
# Una carta se puede jugar si el número de la carta es igual al mazo
# o el color de la carta es igual del mazo
