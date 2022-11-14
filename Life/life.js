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
      fill(this.x*16, this.y*3+120, 140);

      strokeWeight(0.5);
    }
    rect(this.x * this.tam, this.y * this.tam, this.tam, this.tam);
    fill(0);
    textSize(escala);
    text(this.vecinos, this.x * escala, (this.y + 1) * escala);
  }

  paredSup() {
    if (this.y == 0) {
      return true;
    }
  }

  paredInf() {
    if (this.y == height / escala - 1) {
      return true;
    }
  }

  paredIzq() {
    if (this.x == 0) {
      return true;
    }
  }

  paredDer() {
    if (this.x == width / escala - 1) {
      return true;
    }
  }

  contarVecinos() {
    //cuenta cuando no esta en ninguna pared
    if (
      !(
        this.paredDer() ||
        this.paredIzq() ||
        this.paredSup() ||
        this.paredInf()
      )
    ) {
      let acum = 0;
      for (let i = -1; i <= 1; i++) {
        for (let j = -1; j <= 1; j++) {
          if (!(i == 0 && j == 0)) {
            acum += celulas[this.x + i][this.y + j].viva;
          }
        }
      }
      this.vecinos = acum;
    }
    //contar para cuando esta en las esquinas
    else if (this.paredSup() && this.paredDer()) {
      //esquina superior derecha
      this.vecinos =
    } else if (this.paredSup() && this.paredIzq()) {
      //esquina superior izquierda
      this.vecinos =
    } else if (this.paredInf() && this.paredIzq()) {
      //esquina inf izquierda
      this.vecinos =
    } else if (this.paredInf() && this.paredDer()) {
      //esquina inf der
      this.vecinos =
    } else if (this.paredSup()) {
      //pared superior
        this.vecinos =
    } else if (this.paredIzq()) {
      //pared izquierda
        this.vecinos =
    } else if (this.paredInf()) {
      //pared inferior
      this.vecinos =
    } else if (this.paredDer()) {
      //pared superior
      this.vecinos =
    }
  }

let celulas;
let columnas;
let filas;
let escala = 20;

function setup() {
  noLoop();
  createCanvas(600, 600);
  columnas = width / escala;
  filas = height / escala;
  //creo la matriz
  celulas = new Array(filas);
  for (let i = 0; i < celulas.length; i++) {
    celulas[i] = new Array(columnas);
  }

  //inicializo la matriz con células
  for (let i = 0; i < filas; i += 1) {
    for (let j = 0; j < columnas; j += 1) {
      celulas[i][j] = new Celula(i, j, escala);
    }
  }
}

function draw() {
  background(0);

  //muestro la matriz de celulas
  for (let i = 0; i < filas; i += 1) {
    for (let j = 0; j < columnas; j += 1) {
      celulas[i][j].contarVecinos();
      celulas[i][j].show();
      //console.log(celulas[i][j].vecinos)
    }
  }
}
