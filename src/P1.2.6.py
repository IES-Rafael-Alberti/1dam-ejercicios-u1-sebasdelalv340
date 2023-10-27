"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""

def main():

    precio_total = int(input("Introduzca el importe del artículo: "))

    coste_sin_iva = precio_total / 1.1
    coste_iva = precio_total - coste_sin_iva

    print(f"El importe del IVA es {coste_iva:.2f} y el importe sin IVA es {coste_sin_iva:.2f}.")

if __name__ == "__main__":
    main()