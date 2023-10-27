"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo."""

def main():

    precio = int(input("Introduzca el precio sin IVA: "))
    iva = int(input("Introduzca el IVA: "))

    precio_iva = precio * iva / 100
    precio_total = precio + precio_iva
    print(precio_total)

if __name__ == "__main__":
    main()