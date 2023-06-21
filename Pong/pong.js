class Paleta {
  
    constructor(x,y) {
    this.x = x
    this.y = y
    this.vel = 2
    this.tam = 120
    }
  
    show() {
      rect(this.x, this.y, this.tam, this.tam / 3);
    }
    moverIzq() {
      this.x -= this.vel;
    }
    moverDer() {
      this.x += this.vel;
    }
  }
  
  pelota = {
    x: 200,
    y: 200,
    vx: 2,
    vy: 3,
  
    show() {
      ellipse(this.x, this.y, 50, 50);
    },
    rebotarPared() {
      this.vx = -this.vx;
    },
    rebotar() {
      this.vy = -this.vy;
    },
    mover() {
      this.x += this.vx;
      this.y += this.vy;
    },
    reaparecer(){
      this.x =200
      this.y =200
      this.vy= -this.vy
    }
  };
  
  paleta1 = new paleta(200,450)
  
  function setup() {
    createCanvas(400, 500);
  }
  
  function draw() {
    background(220);
    paleta1.show();
    pelota.show();
    pelota.mover();
    
    //chequeo de paredes
    if (pelota.x > 400 || pelota.x < 0) {
      pelota.rebotarPared();
    }
    
    //chequeo si fuera de limites
    if (pelota.y> 500 || pelota.y<0){
      pelota.reaparecer()
    }
    
    //configuracion de controles para j1
    if (keyIsPressed && key == "a") {
      paleta1.moverIzq();
    }
    if (keyIsPressed && key == "d") {
      paleta1.moverDer();
    }
    
    //chequeo de colisiones
    if (pelota.x > paleta1.x && pelota.x < paleta1.x+paleta1.tam && pelota.y>paleta1.y){
      pelota.rebotar()
    }
    
    
  }
  