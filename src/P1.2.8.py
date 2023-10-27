"""Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes."""

def main():

    n1 = int(input("Introduce un número: "))
    n2 = n1
    n1 = int(input("Introduce un número: "))
    n2 = n2 + n1
    n1 = int(input("Introduce un número: "))
    n2 = n2 + n1

    print(n2)

if __name__ == "__main__":
    main()