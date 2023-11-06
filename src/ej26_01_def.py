"""Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta."""


def obtener_lista_compra_distintas_lineas(lista):
    lista = lista.replace(",", "\n")
    return lista

def main():
    lista = input("Introduce la cesta de la compra separando los productos por comas: ")    
    print(obtener_lista_compra_distintas_lineas(lista))

if __name__ == "__main__":
    main()