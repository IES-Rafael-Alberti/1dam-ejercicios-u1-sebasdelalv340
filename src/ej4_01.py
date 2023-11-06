"""Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida"""

def main():

    grados = int(input("Introduce la temperatura actual: "))

    grados = grados * 9 / 5 + 32

    print(grados, "ºF")

if __name__ == "__main__":
    main()