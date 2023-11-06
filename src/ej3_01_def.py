"""Ejercicio 1.2.3
Suponiendo que se han ejecutado las sentencias de asignación:"""

def obtener_division(ancho, alto):
    a = ancho / 2 # valor = 8.5 y tipo float
    return a

def obtener_cociente(ancho, alto):
    b = ancho // 2 # valor = 8 y tipo int
    return b

def main():
    ancho = 17
    alto = 12.0
    c = alto / 3 # valor = 4.0 y tipo float
    d = 1 + 2 * 5 # valor = 11 y tipo int

    print(obtener_division())
    print(type(obtener_division(ancho, alto)))
    print(obtener_cociente(ancho, alto))
    print(type(obtener_cociente(ancho, alto)))
    print(c)
    print(type(c))
    print(d)
    print(type(d))

if __name__ == "__main__":
    main()