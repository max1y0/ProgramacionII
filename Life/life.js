class Celula {
  }
  
  let celulas
  let columnas
  let filas
  
  function setup() {
    createCanvas(400, 400);
    columnas = width / 10
    filas = height / 10
    
    //creo la matriz
    celulas = new Array(filas);
    for (let i = 0; i < celulas.length; i++) {
      celulas[i] = new Array(columnas);
    }
    
    //inicializo la matriz con células
    for (let i = 0; i < filas; i += 1) {
      for (let j = 0; j < columnas; j += 1) {
        celulas[i][j] = new Celula(i,j,10);
      }
    }
  }
  
  function draw() {
    background(220);
    
    //muestro la matriz de celulas
    for (let i = 0; i < filas; i += 1) {
      for (let j = 0; j < columnas; j += 1) {
        celulas[i][j].show()
      }
    }
  }
  