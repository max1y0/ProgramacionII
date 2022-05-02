let contador = 0

document.getElementById('contador').innerHTML = contador
document.getElementById('boton').addEventListener("click", aumentar);
document.getElementById('cursor').addEventListener("click", comprarCursor);


function aumentar(){
	contador = contador +1
	document.getElementById('contador').innerHTML = contador
}

function comprarCursor(){
	console.log("compre un cursor :)")
}