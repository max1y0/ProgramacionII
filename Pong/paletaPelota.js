paleta = {
    x: 200,
    y: 400,
    vel: 2,
    tam: 120,
  
    show() {
      rect(this.x, this.y, this.tam, this.tam / 3);
    },
    moverIzq() {
      this.x -= this.vel;
    },
    moverDer() {
      this.x += this.vel;
    },
  };
  
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
    mover() {
      this.x += this.vx;
      this.y += this.vy;
    },
  };
  function setup() {
    createCanvas(400, 500);
  }
  
  function draw() {
    background(220);
    paleta.show();
    pelota.show();
    pelota.mover();
    if (pelota.x > 400 || pelota.x < 0) {
      pelota.rebotarPared();
    }
    if (keyIsPressed && key == "a") {
      paleta.moverIzq();
    }
    if (keyIsPressed && key == "d") {
      paleta.moverDer();
    }
  }
  