"""Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

def main():

    n1 = int(input("Introduce un número: "))
    n2 = int(input("Introduce otro número: "))

    if n1 == n2:
        print("Error : Los números no pueden ser iguales.")
    elif n1 < n2:
        n_numeros = n2 - n1
        print(f"El número menos es el {n1} y entre ellos existen {n_numeros} números enteros.")
    else:
        n_numeros = n1 - n2
        print(f"El número menos es el {n2} y entre ellos existen {n_numeros} números enteros.")

if __name__ == "__main__":
    main()
