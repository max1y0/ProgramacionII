class Fraccion {
	constructor (num, denom){
		this.num = num
		this.denom = denom
	}

	sumar(fraccion2){
		let res = new Fraccion(1,1)
		res.num = this.num * fraccion2.denom + this.denom * fraccion2.num
		
		return res
	}

	restar(fraccion2){
		let res = new Fraccion(1,1)
		res.num = this.num * fraccion2.denom + this.denom * (-fraccion2.num)
		res.denom = this.denom * fraccion2.denom
		return res
	}

	dividir(fraccion2){
		let res = new Fraccion(1,1)
		res.num = this.num * fraccion2.denom
		res.denom = this.denom * fraccion2.num
		return res
	}

	multiplicar(fraccion2){
		let res = new Fraccion(1,1)
		res.num = this.num * fraccion2.num
		res.denom = this.denom * fraccion2.denom
		return res
	}
}

document.getElementById('suma').addEventListener("click", resolverSuma);

function ResolverSuma(){
	let fraccion1 = new Fraccion(document.getElementById("fraccion1Num").value,document.getElementById("fraccion1Denom").value)
	let fraccion2 = new Fraccion(document.getElementById("fraccion2Num").value,document.getElementById("fraccion2Denom").value)
	mostrar(fraccion1.sumar(fraccion2))
}


function mostrar(fraccion){
	document.getElementById('resNum').innerHTML = fraccion.num
	document.getElementById('resDenom').innerHTML = fraccion.denom
}
