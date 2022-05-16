let contador = 0
let cursor = {
	cantidad: 0,
	CPS: 0.1,
	precio:15,
	precioMejora: 50
}

document.getElementById('contador').innerHTML = contador
document.getElementById('boton').addEventListener("click", aumentar);
document.getElementById('cursor').addEventListener("click", comprarCursor);
document.getElementById('mejoraCursor').addEventListener("click", mejorarCursor);



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

function mejorarCursor(){
	if ( contador > cursor.precioMejora ) {
		contador = contador - cursor.precioMejora
		cursor.precioMejora = Math.floor(cursor.precioMejora * 1.8)
		cursor.CPS = cursor.CPS * 1.5
		document.getElementById('contador').innerHTML = contador
		document.getElementById('mejoraCursor').innerHTML = 'Mejorar cursor CPS: ' + cursor.CPS.toFixed(2) + ' = ' + cursor.precioMejora

	}
}

function autoclick(){
	//
}

window.setInterval(function(){
    autoclick();
}, 1000);