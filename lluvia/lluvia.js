class Gota {
  constructor (x, y) {
    this.x = x
      this.y = y
      this.tam = random(7,15)
      this.vel = 2
  }
  show() {
    fill(120,180,220)
    rect(this.x, this.y, this.tam/3, this.tam)
  }
  caer() {
    this.y = this.y + this.vel + this.tam/4 
      if (this.y > 400) {
      this.y = 0
    }
  }
}

class granizo extends Gota{
  constructor(x,y){
    super(x,y)
    this.vel =16
    this.tam = random(2,5)
  }

  show(){
    fill(255)
    ellipse(this.x,this.y,this.tam,this.tam)
  }
}

let gotas = []
  function setup() {
  createCanvas(400, 400)
    for (let i = 0; i < 400; i+=1) {
    gotas[i] = new granizo(i, random(-400,0))
  }
}


function draw() {
  background(20)
   for (let i = 0; i < 400; i+=1) {
    gotas[i].show()
    gotas[i].caer()
  }
}
