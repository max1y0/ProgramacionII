from fraccion import Fraccion

def carga(i):
  auxnum = int(input("ingrese el numerador "+str(i)+"\n"))
  auxden = 0 
  while (auxden == 0):
    auxden=int(input("ingrese el denominador "+str(i)+"- no puede ser cero \n"))
  return Fraccion(auxnum,auxden)

fraccion1 = carga(1)
fraccion2 = carga(2)

fraccion1.mostrar()
fraccion2.mostrar()
opcion = int(input("1. sumar \n 2. restar \n 3. multiplicar \n 4. dividir \n"))

if (opcion==1): 
  resultadoSuma = fraccion1.sumar(fraccion2)
  print("la suma es:")
  resultadoSuma.mostrar()
elif(opcion ==2):
  resultadoResta = fraccion1.resta(fraccion2)
  print("La resta es:")
  resultadoResta.mostrar()
elif(opcion==3):
  resultadoMulti = fraccion1.multiplicacion(fraccion2)
  print("la multiplicacion es:")
  resultadoMulti.mostrar()
elif(opcion==4):
  resultadoDiv = fraccion1.division(fraccion2)
  print("La division es:")
  resultadoDiv.mostrar()
else:
  print("error")

