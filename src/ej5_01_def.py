"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

def obtener_precio_con_iva(precio, iva):
    precio_total = precio * (1 + iva / 100)
    return precio_total

def main():
    precio = int(input("Introduzca el precio sin IVA: "))
    iva = int(input("Introduzca el IVA: "))
    print(obtener_precio_con_iva(precio, iva), "ºF")

if __name__ == "__main__":
    main()