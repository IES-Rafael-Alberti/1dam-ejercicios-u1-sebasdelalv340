"""Ejercicio 1.2.3
Suponiendo que se han ejecutado las sentencias de asignación:"""

def main():
    
    ancho = 17
    alto = 12.0

    a = ancho / 2 # valor = 8.5 y tipo float
    b = ancho // 2 # valor = 8 y tipo int
    c = alto / 3 # valor = 4.0 y tipo float
    d = 1 + 2 * 5 # valor = 11 y tipo int

    print(a)
    print(type(a))
    print(b)
    print(type(b))
    print(c)
    print(type(c))
    print(d)
    print(type(d))

if __name__ == "__main__":
    main()