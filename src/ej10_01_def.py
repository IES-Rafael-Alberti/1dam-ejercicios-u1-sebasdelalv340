"""Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética"""

def obtener_calculo():
    resultado = ((3 + 2) / (2 * 5)) ** 2
    return resultado

def main():
    print(obtener_calculo())

if __name__ == "__main__":
    main()