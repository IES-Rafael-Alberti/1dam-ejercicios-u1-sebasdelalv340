"""Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas."""

pan_ayer = int(input("Introduce el número de barras no frescas: "))

pan = 3.49

print(f"El precio habitual es de {pan}, el descuento aplicado es de {pan * 0.6:.2f} y el coste final de las barras es {((pan_ayer * pan) - (pan * 0.6)):.2f}.")