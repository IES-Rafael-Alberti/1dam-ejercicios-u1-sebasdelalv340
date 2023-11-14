"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas."""

def obtener_descuento(pan, descuento):
    cantidad_descuento = pan * descuento
    return cantidad_descuento

def obtener_descuento_aplicado(pan, descuento):
    descuento_aplicado = pan * (1 - descuento)
    return descuento_aplicado

def main():
    pan_ayer = int(input("Introduce el número de barras no frescas: "))
    pan = int(input("Introduce cual es el coste del pan: "))
    descuento = float(input("Introduce el descuento: "))

    print(f"El precio habitual es de {pan}, el descuento aplicado es de {obtener_descuento(pan, descuento):.2f} y el coste final de las barras es {(pan_ayer * (obtener_descuento_aplicado())):.2f}.")

if __name__ == "__main__":
    main()