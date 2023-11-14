"""Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado."""

def obtener_peso_total(p):
    peso_total = p * 112
    return peso_total

def obtener_peso_total(m):
    peso_total = m * 75
    return peso_total

def main():
    p = int(input("Introduce el número de payasos: "))
    m = int(input("Introduce el número de muñecas: "))

    print("El peso total es de", (obtener_peso_total(p) + obtener_peso_total(m)), "g.")

if __name__ == "__main__":
    main()