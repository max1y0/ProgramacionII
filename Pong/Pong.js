class Paleta{
  constructor(pX){
    this.pX = pX
    this.pY = height/2
    this.velX = 2
    this.velY = 2
  }
  
  show(){
    rect(this.pX,this.pY,30,90)
  }
  
  rebotarPared(){
    this.velX = -this.velX
  }
  
  rebotarTechoYPiso(){
    this.velY = -this.velY
  }
  
  moverArr(){
    this.pY = this.pY - this.velY
  }
  
  moverAb(){
    this.pY = this.pY + this.velY
  }
}

let paleta1
let paleta2
function setup() {
  createCanvas(600,400)
  paleta1 = new Paleta(30)
  paleta2 = new Paleta(540)
}


function draw() {
  background('#212121')
  paleta1.show()
  paleta2.show()
  
  if (keyIsPressed && key == 'w') {
    paleta1.moverArr()
  }
  if (keyIsPressed && key == 's') {
    paleta1.moverAb()
  }
  
  if (keyIsPressed && key == 'i') {
    paleta2.moverArr()
  }
  if (keyIsPressed && key == 'k') {
    paleta2.moverAb()
  }
}
