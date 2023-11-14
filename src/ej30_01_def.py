"""Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que pida un número de inicio, un incremento y un total de la serie.
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

def mayorCero (incremento, total_serie):
    while incremento <=0 or total_serie <= 0:
        print("Error: El incremento y el total de la serie deben ser mayor a cero.")

def serieCreciente (n, incremento, total_serie):
    serie = ("Serie ==> ") + str(n)
    while n < total_serie:
        n = n + incremento
        serie = serie + ("-") + str(n)
    else:
        return serie

def main():

    n = int(input("Introduce un número: "))
    incremento = int(input("Introduce un incremento: "))
    total_serie = int(input("Introduce el total de la serie: "))
    mayorCero(incremento, total_serie)
    print(serieCreciente (n, incremento, total_serie))

if __name__ == "__main__":
    main()