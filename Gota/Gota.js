class Gota {
  constructor (x, y) {
      this.x = x
      this.y = y
      this.tam = 8
      this.vel = 2
  }
  show() {
    fill(120, 180, 220)
    rect(this.x, this.y, this.tam/3, this.tam)
  }
  caer() {
    this.y = this.y + this.ve4l //+ this.tam/4
    if (this.y > 400) {
      this.y = 1
    }
  }
}


let gota
  function setup() {
  noStroke()
    createCanvas(400, 400)
    gota = new Gota(200, 1)
}


function draw() {
  background('#BBF1FA')
  gota.show()
      gota.caer()
  
}
