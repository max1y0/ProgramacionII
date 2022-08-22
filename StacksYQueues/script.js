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

class Cola{
	constructor (){
		this.size = 0
		this.datos = []
	}

	esVacia() {
		return this.size == 0
	}

	encolar(x) {
		this.datos[this.size] = x
		this.size++
	}

	consultar(){
		return this.datos[0]
	}

	desencolar(){
		for (var i = 0; i < this.size - 1; i++) {
			this.datos[i] = this.datos[i+1]
		}
		this.size--
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

//COLAS

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


document.getElementById('filtrar-pila').addEventListener("click", filtrarP);
document.getElementById('fusionar-pila-cola').addEventListener("click", fusion);
document.getElementById('verC-sinBorrar').addEventListener("click", verCSinBorrar);
document.getElementById('verP-sinBorrar').addEventListener("click", verPSinBorrar);

function filtrarP (){
//esta funcion deberia pasar todos los elementos pares a una pilaPares
//y los impares a la pilaImpares
    pilaImpares = new Pila()
    pilaPares = new Pila()


//al final hacemos un console log para testear el funcionamiento correcto
	console.log(pilaPares)
	console.log(pilaImpares)
}

function fusion(){
//esta funcion toma los elementos de la cola1 y la pila1, y los guarda en
//una pila final. Es decir pilaFinal, tiene que tener los elementos de
//pila1 y cola1 juntos.
	pilaFinal = new Pila()


//al final hacemos un console log para testear el funcionamiento correcto
	console.log(pilaFinal)
}

function verCSinBorrar(){
//esta funcion debe mostrar los elementos de la Cola, y que al final la
//pila quede como estaba en su estado inicial

//al final hacemos un console log para testear el funcionamiento correcto
	console.log(cola1)
}

function verPSinBorrar(){
//esta funcion debe mostrar los elementos de la Pila, y que al final la
//pila quede como estaba en su estado inicial

//al final hacemos un console log para testear el funcionamiento correcto
	console.log(pila1)
}
