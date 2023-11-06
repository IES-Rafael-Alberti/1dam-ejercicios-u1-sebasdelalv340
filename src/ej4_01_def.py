"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida"""

def obtener_tempertura(grados):
    grados = grados * 9 / 5 + 32
    return grados

def main():
    grados = int(input("Introduce la temperatura actual: "))
    print(grados, "ºF")

if __name__ == "__main__":
    main()