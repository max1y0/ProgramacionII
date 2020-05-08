from fraccion import Fraccion

fraccion1 = Fraccion(2,3)
fraccion2 = Fraccion(4,5)

resultadoSuma = fraccion1.sumar(fraccion2)
resultadoResta = fraccion1.resta(fraccion2)
resultadoMulti = fraccion1.multiplicacion(fraccion2)
resultadoDiv = fraccion1.division(fraccion2)

print("la suma es:")
resultadoSuma.mostrar()
print("La resta es:")
resultadoResta.mostrar()
print("la multiplicacion es:")
resultadoMulti.mostrar()
print("La division es:")
resultadoDiv.mostrar()
