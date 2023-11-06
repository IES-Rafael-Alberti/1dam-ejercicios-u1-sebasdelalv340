"""Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida."""

def main():

    frase = input("Introduce una frase: ")

    print(frase[::-1])

if __name__ == "__main__":
    main()