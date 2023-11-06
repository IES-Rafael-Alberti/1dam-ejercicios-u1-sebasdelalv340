"""Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma."""

def main():

    num1 = int(input("Introduces un número: "))
    num2 = int(input("Introduces otro número: "))
    num3 = int(input("Introduces otro número: "))
    
    print("La suma de tus número es:", num1 + num2 + num3)

if __name__ == "__main__":
    main()