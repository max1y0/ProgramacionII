let contador = 0
let cursor = {
	cantidad: 0,
	CPS: 0.1,
	precio:15
}

document.getElementById('contador').innerHTML = contador
document.getElementById('boton').addEventListener("click", aumentar);
document.getElementById('cursor').addEventListener("click", comprarCursor);


function aumentar(){
	contador = contador +1
	document.getElementById('contador').innerHTML = contador
}

function comprarCursor(){
	if ( contador >= cursor.precio ) {
		contador = contador - cursor.precio
		cursor.precio = Math.floor(cursor.precio * 1.3)
		cursor.cantidad += 1
		document.getElementById('contador').innerHTML = contador
		document.getElementById('cursor').innerHTML = 'Cursor ' + cursor.precio
	}
}