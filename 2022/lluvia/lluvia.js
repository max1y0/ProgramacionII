class Gota {
  constructor (x, y) {
    this.x = x
      this.y = y
      this.tam = random(7, 15)
      this.vel = 2
  }
  show() {
    fill(120, 180, 220)
      rect(this.x, this.y, this.tam/3, this.tam)
  }
  caer() {
    this.y = this.y *random(1,1.1)//+ this.vel + this.tam/4
      if (this.y > 400) {
      this.y = 1
    }
  }
}

class sakura extends Gota {
  constructor(x, y) {
    super(x, y)
      this.vel =2
      this.tam = random(5, 10)
      //this.color = [random(230, 250), random(160, 180), random(230, 250)]
      this.img = loadImage('petal.png');
  }

  show() {
    //tint(this.color)
      image(this.img, this.x, this.y,this.tam,this.tam)
      //ellipse(this.x,this.y,this.tam,this.tam)
  }
}

let gotas = []
  function setup() {
  noStroke()
    createCanvas(400, 400)
    for (let i = 0; i < 400; i+=1) {
    gotas[i] = new sakura(i, 1)
  }
}


function draw() {
  background('#BBF1FA')
    for (let i = 0; i < 400; i+=1) {
    gotas[i].show()
      gotas[i].caer()
  }
}
