
import random


class mastermind:
    def __init__(self):
        self.fichas = []

    def inicializar(self,lista):
        self.fichas = lista

    def inicializarRandom (self, dificultad):
        if (dificultad.lower() == "facil"):
            for _ in range(4): 
                ficha = random.choice(["rojo","azul","verde","amarillo"])
                while ficha in self.fichas:
                    ficha = random.choice(["rojo","azul","verde","amarillo"])
                self.fichas.append(ficha)
        elif (dificultad.lower() == "medio"):
            for _ in range(4): 
                ficha = random.choice(["rojo","azul","verde","amarillo"])
                self.fichas.append(ficha)
        else:
            for _ in range(4): 
                self.fichas.append(random.choice(["rojo","azul","verde","amarillo","naranja","lila"]))
    
    def chequeo (self,solucion):
        fichas = self.fichas[:]
        pista = ["errado","errado","errado","errado"]
        for i in range (len(solucion)):
            for j in range ( len(fichas) ):
                # print(solucion[i],i,fichas[j],j)
                if solucion[i] == fichas[j] and i == j:
                    pista [i] = "toque"
                    fichas[j] = " "
                    break
        for i in range (len(solucion)):
            for j in range ( len(fichas) ):
                # print(solucion[i],i,fichas[j],j)
                if solucion[i] == fichas[j] and pista[i] != "toque":
                    pista[i] = "roce"
                    fichas[j] = " "
                
        pista.sort()
        return pista
    
    def mostrar(self):
        print(self.fichas)
    
                

#de aca  completar el codigo principal