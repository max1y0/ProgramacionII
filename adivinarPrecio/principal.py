from producto import Producto

print ("probando clase producto")

producto1 = Producto()

print ("creado objeto producto1")

producto1.generarPrecio()

print("generado el precio aleatorio.")
print("en este caso el precio es de",producto1.precio)

print("Generando el nombre aleatorio")
producto1.generarNombre()

print("El nombre generado es", producto1.nombre)
