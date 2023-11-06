"""Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""

def obtener_ahorro_acumulado(ahorro, interes):
    primer_año = (ahorro * interes) + ahorro
    return primer_año

def main():
    ahorro = float(input("Introduce el balance de tu cuenta: "))
    interes = float(input("Introduce el interés: "))

    segundo_año = (obtener_ahorro_acumulado(ahorro, interes) * interes) + obtener_ahorro_acumulado(ahorro, interes)
    tercer_año = (segundo_año * interes) + segundo_año

    print("El balance de la cuenta tras el primer año es {:.2f} ,el segundo es {:.2f} y el tercero es {:.2f} ".format(obtener_ahorro_acumulado(), segundo_año, tercer_año))

if __name__ == "__main__":
    main()