class Pila {
	constructor (){
		this.size = 0
		this.datos = []
	}

	esVacia () {
		return this.size == 0
	}

	tope() {
		if (!(this.esVacia())) {
			return this.datos[this.size-1]
		}
	}

	apilar(x) {
		this.datos[this.size] = x
		this.size++
	}

	desapilar() {
		if (!(this.esVacia())) {
			this.size--
		}
	}

	//vaciar()

}

let pila1 = new Pila()


document.getElementById('apilar').addEventListener("click", apilado);
document.getElementById('desapilar').addEventListener("click", desapilado);
document.getElementById('tope').addEventListener("click", verTope);
document.getElementById('ver').addEventListener("click", ver);

function apilado(){
	const x = document.getElementById("item").value
	document.getElementById("item").value = 0
	pila1.apilar(x)
}

function desapilado(){
	pila1.desapilar()
}

function verTope(){
	const x = pila1.tope()
	document.getElementById('topeItem').innerHTML = x
}

function ver(){
	//como hacer para que pila1 no pierda todos los elementos??
	const lista = document.getElementById("items")
	lista.innerHTML = ""
	while ( !pila1.esVacia() ) {
		const item = document.createElement("li")
		item.innerText = pila1.tope()
		pila1.desapilar()
		lista.appendChild(item)
	}
}

//COLAS

class Cola{
	constructor (){
		this.size = 0
		this.datos = []
	}

	esVacia() {
	}

	encolar(x) {
	}

	consultar(){
	}

	desencolar(){
	}
}

cola1 = new Cola();

document.getElementById('encolar').addEventListener("click", encolado);
document.getElementById('desencolar').addEventListener("click", desencolado);
document.getElementById('consultar').addEventListener("click", verPrimer);
document.getElementById('verC').addEventListener("click", verC);

function encolado(){
	const x = document.getElementById("itemC").value
	document.getElementById("itemC").value = 0
	cola1.encolar(x)
}

function desencolado(){
	cola1.desencolar();
}

function verPrimer(){
	const x = cola1.consultar()
	document.getElementById('primero').innerHTML = x
}

function verC(){
	//como hacer para que pila1 no pierda todos los elementos??
	const lista = document.getElementById("itemsC")
	lista.innerHTML = ""
	while ( !cola1.esVacia() ) {
		const item = document.createElement("li")
		item.innerText = cola1.consultar()
		cola1.desencolar()
		lista.appendChild(item)
	}
}

