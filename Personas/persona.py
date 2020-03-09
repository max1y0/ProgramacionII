class Persona:

    # nombre = None
    # apellido = None
    # anio_nac = None
    
    def __init__(self,nombre,apellido,anio_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.anio_nac = anio_nac

    def decirNombre(self):
        return self.nombre+self.apellido

    def decirEdad(self):
        return 2020 - self.anio_nac