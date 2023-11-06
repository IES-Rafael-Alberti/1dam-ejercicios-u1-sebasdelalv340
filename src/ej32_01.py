
#
# Ejercicio 1.32 - Lee dos números y crea la serie que los une de 1 en 1...
#

"""> Introduce un número: 4
> Introduce otro: 8
> 4-5-6-7-8

> Introduce un número: 12
> Introduce otro: 3
> 3-4-5-6-7-8-9-10-11-12

Inicio

	Escribe "Introduce un número: "
	Lee x
	Escribe "Introduce otro: "
	Lee y
	
	Si (x >= y) entonces
		numIni = x
		numFin = y
	Sino
		numIni = y
		numFin = x
		
	Mientras (numIni <= numFin) hacer
		Escribe numIni
		Si (numIni != numFin) entonces
			Escribe "-"
                numIni = numIni + 1

Fin"""

def main():

    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))

    if n1 <= n2:
        num_inicio = n1
        num_fin = n2
    else:
        num_inicio = n2
        num_fin = n1

    """while num_inicio <= num_fin:
        print(num_inicio)
        if num_inicio != num_fin:
            print("-")
        num_inicio = num_inicio + 1"""
    
    serie = num_inicio

    while num_inicio < num_fin:
        num_inicio = num_inicio + 1
        serie = str(serie) + "-" + str(num_inicio)
    else:
        print(serie)  


if __name__ == "__main__":
    main()