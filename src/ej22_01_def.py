"""Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula."""

def obtener_caracter_mayuscula(frase):
    frase = frase[:-1] + frase[-1].upper()
    return frase

def main():
    frase = input("Introduce una frase y una vocal: ")
    print(obtener_caracter_mayuscula(frase))

if __name__ == "__main__":
    main()