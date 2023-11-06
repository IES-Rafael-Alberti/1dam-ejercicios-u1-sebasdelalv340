"""Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida."""

def invertir_cadena(frase):
    frase_invertida = frase[::-1]
    return frase_invertida

def main():
    frase = input("Introduce una frase: ")
    print(invertir_cadena(frase))

if __name__ == "__main__":
    main()