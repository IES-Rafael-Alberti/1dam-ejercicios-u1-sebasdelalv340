"""Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión."""

def obtener_telefono(telefono):
    tlf = telefono[4:-3]
    return tlf

def main():
    telefono = input("Introduzca su número de telefono como en el ejemplo (+34-913724710-56): ")
    print(obtener_telefono(telefono))

if __name__ == "__main__":
    main()