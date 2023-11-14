"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

def obtener_parte_entera(precio):
    euros = precio.split(".")[0]
    return euros

def obtener_parte_decimal(precio):
    centimos = precio.split(".")[-1]
    return centimos

def main():
    precio = input("Introduce un precio: ")   
    print(f"{obtener_parte_entera(precio)} euros y {obtener_parte_decimal(precio)} céntimos.")

if __name__ == "__main__":
    main()