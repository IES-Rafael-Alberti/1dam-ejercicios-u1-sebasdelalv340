"""Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre."""

def contar_caracteres(nombre):
    n = len(nombre)
    return n

def main():
    nombre = input("Introduzca su nombre: ")
    print(f"{nombre} tiene {contar_caracteres(nombre)} letras.")

if __name__ == "__main__":
    main()