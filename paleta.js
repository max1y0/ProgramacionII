paleta ={
  x: 200,
  y: 400,
  vel: 2,
  tam:120,
  
  show(){
    rect(this.x,this.y,this.tam,this.tam/3)
  },
  moverIzq(){
    this.x -= this.vel
  },
  moverDer(){
    this.x += this.vel
  }
}

function setup() {
  createCanvas(400, 500);
}

function draw() {
  background(220);
  paleta.show()
  if (keyIsPressed && key == 'a'){
      paleta.moverIzq()
    }
  if (keyIsPressed && key == 'd'){
      paleta.moverDer()
    }
}
