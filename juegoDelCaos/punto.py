class punto:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        
    def mostrar(self):
        strokeWeight(2)
        point(self.x,self.y)
