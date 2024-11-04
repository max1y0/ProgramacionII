class Pila:
    def __init__(self,tamanio):
        self.tamanio = tamanio
        self.lista = []

    def es_vacia(self):
        return len(self.lista) == 0
        #retorna verdadero si es vacía

    def tope(self):
        if not (self.es_vacia()):
            return self.lista[-1]
        else:
            print("pila vacia bro")
        #si no está vacía, retorna el elemento que esta al final de la lista

    def apilar(self, x):
        if len(self.lista) < self.tamanio:
            self.lista.append(x)
        else:
            print("pila llena bro")
        #si no está llena, ingresa el elemento x al final de la lista

    def desapilar(self):
        if not (self.es_vacia()):
            self.lista.pop()
        else:
            print("pila vacia bro")
        #si no está vacía, elimina el elemento al final de la lista

    def es_llena(self):
        return len(self.lista) == self.tamanio
        #retorna verdadero si el tamaño de la lista es igual al tamaño de la pila
