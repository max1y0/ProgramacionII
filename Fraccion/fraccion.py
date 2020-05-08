class Fraccion:

    def __init__ (self, num, den):
        self.numerador = num
        self.denominador = den

    def mostrar (self):
        print (self.numerador,"/",self.denominador)

    def sumar (self, fraccion2):
        #inicializo la variable resultado
        resultado = Fraccion(1,1)
        #metodo mariposa
        resultado.numerador = self.numerador * fraccion2.denominador + fraccion2.numerador * self.denominador
        resultado.denominador = self.denominador * fraccion2.denominador
        return resultado

    def resta (self, fraccion2):
        #inicializo la variable resultado
        resultado = Fraccion(1,1)
        #metodo mariposa para restas
        resultado.numerador = self.numerador * fraccion2.denominador - fraccion2.numerador * self.denominador
        resultado.denominador = self.denominador * fraccion2.denominador
        return resultado
   
    def division (self, fraccion2):
        #inicializo la variable resultado
        resultado = Fraccion(1,1)
        #división
        resultado.numerador = self.numerador * fraccion2.denominador
        resultado.denominador = self.denominador * fraccion2.numerador
        return resultado

    def multiplicacion (self, fraccion2):
        #inicializo la variable resultado 
        resultado = Fraccion(1,1)
        #multiplico
        resultado.numerador = self.numerador * fraccion2.numerador
        resultado.denominador = self.denominador * fraccion2.denominador
        return resultado


