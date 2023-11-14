"""Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido."""

def obtener_nombre_distintas_lineas(nombre, n):
    serie = ((nombre + "\n") * n)
    return serie

def main():
    nombre = input("Introduce tu nombre: ")
    n = int(input("Introduce un número: "))

    print(obtener_nombre_distintas_lineas(nombre, n))

if __name__ == "__main__":
    main()