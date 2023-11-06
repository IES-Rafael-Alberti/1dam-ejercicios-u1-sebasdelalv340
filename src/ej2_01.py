"""Ejercicio 1.2.2
Escribe un progama para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio."""

def main():
    horas = input("Horas de trabajo: ")
    precio = input("Coste por hora: ")

    suma = int(horas) * int(precio)
    print(suma)

if __name__ == "__main__":
    main()