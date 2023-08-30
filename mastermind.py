import random

#clase mastermind, completar:
class mastermind:
    def __init__(self):
        #completar

    def inicializar(self):
        #completar

    def inicializarRandom (self):
        #completar
    
    def chequeo (self,pos,color):
        #completar
    
    def mostrar(self):
        #completar
    
                

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