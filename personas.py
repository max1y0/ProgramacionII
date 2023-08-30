class Empleado:
    def __init__ (self,nombre,cargo,edad,dni,antiguedad):
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.dni = dni
        self.antiguedad = antiguedad
    
    def anio_nacimiento(self):
        return 2023 - edad

    def categoria():
        if (antiguedad>5):
            return "senior"
        elif (antiguedad <=2):
            return "junior"
        else:
            return "semi-senior"

print("cargando empleado 1")
empleado1 = Empleado(input("Ingrese su nombre "),
                    int(input("Ingrese su edad ")),
                    input("ingrese su cargo "),
                    int(input("Ingrese su dni ")),
                    int(input("Ingrese su antiguedad en el trabajo")))
print("\n\ncargando empleado 2")
empleado1 = Empleado(input("Ingrese su nombre "),
                    int(input("Ingrese su edad ")),
                    input("ingrese su cargo "),
                    int(input("Ingrese su dni ")),
                    int(input("Ingrese su antiguedad en el trabajo")))
print("\n\ncargando empleado 3")
empleado1 = Empleado(input("Ingrese su nombre "),
                    int(input("Ingrese su edad ")),
                    input("ingrese su cargo "),
                    int(input("Ingrese su dni ")),
                    int(input("Ingrese su antiguedad en el trabajo")))
#teniendo estos tres empleados cargados resolver:
#1) Indicar si el segundo y el tercero son colegas (si tienen el mismo cargo)
#2) Indicar la etapa de vida de la primer persona (
#   joven adulto de 18 a 30
#   adulto mayor de 30 a 60
#   adulto mayor de 60 en adelante)
#   y al lado de esto informar su categoría
#3) Comparar las edades e indicar cual es el mas grande de los 3
#4) Comparar los años de antiguedad e informar DNI y nombre, en orden de mayor antiguedad a menor antiguedad