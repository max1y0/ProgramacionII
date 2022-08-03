class Pila {
	constructor (){
		this.size = 0
		this.pila = []
	}

	esVacia () {
		return this.size == 0
	}

	tope() {
		if (!(this.esVacia())) {
			return this.pila[this.size-1]
		}
	}

	apilar(x) {
		this.pila[this.size] = x
		this.size++
	}

	desapilar() {
		if (!(this.esVacia())) {
			this.size--
		}
	}

	//vaciar()

	mostrar() {
		for (var i = 0; i < this.size; i++) {
			console.log(this.pila[i])
		}
	}

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
