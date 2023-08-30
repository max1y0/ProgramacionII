#darles el algoritmo y que ellos hagan la clase
import random

#clase mastermind, completar:
class mastermind:
    def __init__(self):
        self.fichas = []

    def inicializar(self):
        pass

    def inicializarRandom (self):
        for _ in range(4): 
            self.fichas.append(random.choice(["rojo","azul","verde","amarillo","naranja"]))
    
    def chequeo (self,pos,color):
        i = 0
        result = "errado"
        while (i<4 and result !="hit"):
            if (self.fichas[i] == color and i == pos):
                result = "toque"
            elif (color in self.fichas):
                result = "roce"
            i+=1
        return result
    
    def mostrar(self):
        print(self.fichas)
    
                

#de aca en adolante NO TOCAR NADA
juego = mastermind()
print("Cuantos jugadores van a jugar? 1/2")
jugadores = int(input())
if (jugadores == 2):
    print("Que el jugador 2 no vea tu combinacion secreta! \n")
    juego.inicializar()
else:
    juego.inicializarRandom()

intentos = 0
listaPrevios = []
while (intentos < 10):
    solucion = []
    for previos in listaPrevios:
        print(previos)
    solucion = input("\nIngresa tu combinación de colores separados por espacios: \n").split()

    i = 0
    pista = []
    print("----------------------\nla pista según tu solución es: ")
    while (i < 4):
        pista.append(juego.chequeo(i,solucion[i]))
        i+=1
    pista.sort()
    print (pista)
    if (pista.count("toque")>=4):
        print("\ntu solución era correcta!")
        break
    else:
        print(f"\nSolución incorrecta, intenta de nuevo. Intento nro {intentos+1}")
        intentos = intentos + 1
    listaPrevios.append(solucion+pista)
if intentos >=10:
    print ("Perdiste el secreto era \n",juego.mostrar)