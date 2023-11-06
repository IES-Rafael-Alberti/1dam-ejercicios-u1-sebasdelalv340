"""Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:"""

def obtener_suma_serie(n):    
    suma = (n * (n + 1)) / 2
    return suma

def main():
    n = int(input("Introduce un número: "))
    if n < 1:
        print("Error")
    else:
        print(obtener_suma_serie(n))

if __name__ == "__main__":
    main()