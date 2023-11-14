"""Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguiente: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente."""

from src.ej3_01_def import obtener_cociente

def obtener_resto(n, m):
    r = n % m
    return r

def main():
    n = int(input("Introduce un número: "))
    m = int(input("Introduce otro número: "))
    print(f"La división de {n} entre {m} da un cociente {obtener_cociente(n, m)} y n resto {obtener_resto(n, m)}.")

if __name__ == "__main__":
    main()