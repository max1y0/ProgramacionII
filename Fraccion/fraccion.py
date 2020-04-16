class Fraccion:

    def __init__ (self, num, den):
        self.numerador = num
        self.denominador = den

    def mostrar (self):
        print (self.numerador , "/" , self.denominador)

    def sumar (self, fraccion2):
        #inicializo la variable resultado en 1 / 1. Si no se inicializa hay error
        resultado = Fraccion(1,1)

        #metodo mariposa
        resultado.numerador = self.numerador * fraccion2.denominador + fraccion2.numerador * self.denominador
        resultado.denominador = self.denominador * fraccion2.denominador
        return resultado

