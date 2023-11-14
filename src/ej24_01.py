"""Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

def main():

    precio = input("Introduce un precio: ")
    euros = precio.split(".")[0]
    centimos = precio.split(".")[-1]

    print(f"{euros} euros y {centimos} céntimos.")

if __name__ == "__main__":
    main()