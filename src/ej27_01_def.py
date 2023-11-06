"""Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales."""
from ej2_01_def import obtener_salario

def main():
    producto = input("Introduce un producto: ")
    precio = float(input("Introduce su precio: "))
    ud = int(input("Introduce número de unidades: "))

    print(f"El producto {producto} cuesta {precio:7.2f} y {ud:3d} unidades cuestan {obtener_salario(precio, ud):9.2f}.")

if __name__ == "__main__":
    main()