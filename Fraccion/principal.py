from fraccion import fraccion

unumerador = int(input("enter the first numerator"))#variables para cargar el valor de las fracciones
if unumerador == "0":
    a=int(input("re-enter the first non-zero numerator"))#si el usuario ingresa un cero esta variable va a volver a pedir que cambie su numero
    unumerador = a#entonces la variable inicial ya no valera cero si no que pone el otro numero
udenominador = int(input("enter the first denominator"))
if udenominador == "0":
   b=int(input("re-enter the first non-zero denominator"))
   udenominador = b
snumerador = int(input("enter the second numerator"))
if snumerador == "0":
   c=int(input("re-enter the second non-zero numerator"))
   snumerador = c
sdenominador = int(input("enter the second denominator"))
if sdenominador == "0":
   d=int(input("re-enter the second non-zero denominator"))
   sdenominador = d 
    
def menu():
    print ("options the calculators")
    print ("1.Adding the fractions")
    print ("2.Substracction the fractions")
    print ("3.Multiply the fractions")
    opcion = int(input("Enter the options \n"))

    while((opcion>0)and(opcion<4)):
        if opcion==1:
            resultado=fraccion1.sumar(fraccion2)
            print("the addition is:")
            resultado.mostrar()
        elif opcion==2:
            resultado=fraccion1.restar(fraccion2)
            print("the substracction is:")
            resultado.mostrar()
        elif opcion==3:
            resultado=fraccion1.multiplicacion(fraccion2)
            print("the multiply is:")
            resultado.mostrar()
        elif opcion==4:
            print("error")
            break
        opcion =4

fraccion1=fraccion(unumerador,udenominador)
fraccion2=fraccion(snumerador,sdenominador)
fraccion1.mostrar()
fraccion2.mostrar()
menu()
