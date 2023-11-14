"""Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""

def suma_numeros(n1, n2, n3):
    suma = n1 + n2 + n3
    return suma

def main():
    n1 = int(input("Introduces un número: "))
    n2 = int(input("Introduces otro número: "))
    n3 = int(input("Introduces otro número: "))
    print("La suma de tus número es:", suma_numeros(n1, n2, n3))

if __name__ == "__main__":
    main()