"""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""

def main():

    frase = input("Introduce una frase y una vocal: ")

    print(frase[0:-1] + frase[-1].upper())

if __name__ == "__main__":
    main()