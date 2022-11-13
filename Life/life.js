class Celula {
  constructor(x, y, tam) {
    this.x = x;
    this.y = y;
    this.tam = tam;
    this.viva = floor(random(2));
    this.vecinos = 0;
  }
  show() {
    if (this.viva == 0) {
      fill(0);
    } else {
      
      if (this.paredSup()) {
        fill(200, 20, 140);
      }
      if (this.paredInf()) {
        fill(50, 20, 140);
      }
      if (this.paredDer()) {
        fill(50, 220, 140);
      }
      if (this.paredIzq()) {
        fill(50, 120, 140);
      }
      if(!( this.paredDer() || this.paredIzq() || this.paredSup() || this.paredInf())){
      fill(250);
      }
      strokeWeight(0.5);
    }
    rect(this.x * this.tam, this.y * this.tam, this.tam, this.tam);
    fill(0);

    text(this.vecinos, this.x * 10, (this.y + 1) * 10);
  }

  paredSup() {
    if (this.y == 0) {
      return true;
    }
  }

  paredInf() {
    if (this.y == height / 10 - 1) {
      return true;
    }
  }

  paredIzq() {
    if (this.x == 0) {
      return true;
    }
  }

  paredDer() {
    if (this.x == width / 10 - 1) {
      return true;
    }
  }
  
  contarVecinos(){
    //cuenta cuando no esta en ninguna pared
    if( !(this.paredDer() || this.paredIzq() || this.paredSup() || this.paredInf())){
      let acum = 0
      //completar

      this.vecinos = acum
    } else{
      //contar para cuando esta en las paredes
      //completar
    }
  }
}

let celulas;
let columnas;
let filas;

function setup() {
  createCanvas(400, 400);
  columnas = width / 10;
  filas = height / 10;
  //creo la matriz
  celulas = new Array(filas);
  for (let i = 0; i < celulas.length; i++) {
    celulas[i] = new Array(columnas);
  }

  //inicializo la matriz con células
  for (let i = 0; i < filas; i += 1) {
    for (let j = 0; j < columnas; j += 1) {
      celulas[i][j] = new Celula(i, j, 10);
    }
  }
}

function draw() {
  background(0);

  //cuento vecinos y muestro la matriz de celulas
  for (let i = 0; i < filas; i += 1) {
    for (let j = 0; j < columnas; j += 1) {
      celulas[i][j].contarVecinos()
      celulas[i][j].show();
    }
  }
}
