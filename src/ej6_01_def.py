"""Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%)."""

def obtener_precio_sin_iva(precio_total):
    coste_sin_iva = precio_total / 1.1
    return coste_sin_iva

def obtener_iva(precio_total, coste_sin_iva):
    coste_iva = precio_total - coste_sin_iva
    return coste_iva

def main():
    precio_total = int(input("Introduzca el importe del artículo: "))
    print(f"El importe del IVA es {obtener_precio_sin_iva(precio_total):.2f} y el importe sin IVA es {obtener_iva(precio_total):.2f}.")
    
if __name__ == "__main__":
    main()