from punto import punto

puntoA = punto(random(600),random(400))
puntoB = punto(random(600),random(400))
puntoC = punto(random(600),random(400))

origen = punto(random(600),random(400))

def setup():
    size (600,400)
    
def draw():
    for i in range (10):
        stroke(255,0,0)
        puntoA.mostrar()
        puntoB.mostrar()
        puntoC.mostrar()
        stroke(0,0,255)
        origen.mostrar()
        
        opcion = floor(random(3))
        
        if (opcion == 0):
            origen.x = lerp(origen.x,puntoA.x, 0.5)
            origen.y = lerp(origen.y,puntoA.y, 0.5)
        elif ( opcion ==1):
            origen.x = lerp(origen.x,puntoB.x, 0.5)
            origen.y = lerp(origen.y,puntoB.y, 0.5)
        elif ( opcion ==2):
            origen.x = lerp(origen.x,puntoC.x, 0.5)
            origen.y = lerp(origen.y,puntoC.y, 0.5)    
    
