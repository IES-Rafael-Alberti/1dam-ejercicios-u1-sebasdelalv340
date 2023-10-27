"""Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que solicite un nombre y una edad.
Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
El pseudocódigo debes incluirlo como comentarios en el programa de Python."""

def main():

    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))

    while edad <= 0 or edad > 125:
        edad = int(input("Introduce una edad entre 0 y 125: "))
    
    print(f"Te lammas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir.")

if __name__ == "__main__":
    main()