#
# Ejercicio 1.31 - Lee un número hasta que el número esté en el rango 1-10
#

"""> Introduce un número: 15
> Inténtalo otra vez! (1-10): 0
> Inténtalo otra vez! (1-10): 5
> Correcto!

Inicio

	Escribe "Introduce un número: "
	Lee num
	
	Mientras (num < 1 or num > 10)
		Escribe "Inténtalo otra vez! (1-10): "
		Lee num
	Escribe "Correcto!"
	
Fin"""
       

def main():
    
    n = int(input("Introduce un número: "))

    while n < 1 or n > 10:
        n = int(input("Inténtalo otra vez! (1-10): "))
    else:
        print("¡Correcto!")

    
if __name__ == "__main__":
    main()