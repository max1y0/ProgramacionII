class Pelota{
  constructor (pX,pY){
    this.pX = pX
    this.pY = pY
    this.color = [255,255,255]
    this.velX = -2
    this.velY = 2
  }
  
  show(){
    ellipse(this.pX,this.pY,50,50)
  }
  
  rebotarPared(){
    this.velX = -this.velX
  }
  rebotarTechoYPiso(){
    this.velY = -this.velY
  }
}
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
let pelota = new Pelota(200,200)
function setup() {
  createCanvas(600,400)
  paleta1 = new Paleta(30)
  paleta2 = new Paleta(540)
}


function draw() {
  background(21,21,21,20)
  fill(255)
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
  
  pelota.show()
  pelota.pX = pelota.pX + pelota.velX
  pelota.pY = pelota.pY + pelota.velY
  
  //detecto paredes :)
  if(pelota.pY > paleta1.pY && pelota.pY < paleta1.pY + 90
     &&
     pelota.pX < paleta1.pX+30  && pelota.pX > paleta1.pX){
    pelota.rebotarPared()
  }
  //detecto piso y techo
  if(pelota.pY > height || pelota.pY < 20){
    pelota.rebotarTechoYPiso()
  }
}
