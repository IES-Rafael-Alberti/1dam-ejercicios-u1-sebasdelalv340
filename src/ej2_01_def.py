"""Ejercicio 1.2.2
Escribe un progama para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio."""

def obtener_salario(horas, precio):
    total = horas * precio
    return total


def main():
    horas = float(input("Horas de trabajo: "))
    precio = float(input("Coste por hora: "))
    print(obtener_salario(horas, precio))


if __name__ == "__main__":
    main()