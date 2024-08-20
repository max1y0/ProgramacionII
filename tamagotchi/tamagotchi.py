class Tamagotchi:
  def __init__(self,hambre):
    self.hambre =0
    self.salud =0
    self.higiene =0
  
  def alimentar(self):
    self.hambre +=20
    print(self.hambre)
