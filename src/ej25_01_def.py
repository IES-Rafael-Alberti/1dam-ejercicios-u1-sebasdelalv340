"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter."""

def obtener_dia(fecha_completa):
    lista = fecha_completa.split("/")    
    dia = lista[0]
    return dia

def obtener_mes(fecha_completa):
    lista = fecha_completa.split("/")
    mes = lista[1]
    return mes

def obtener_anio(fecha_completa):
    lista = fecha_completa.split("/")
    año = lista[2]
    return año

def main():
    fecha_completa = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    print(f"El día {obtener_dia(fecha_completa)}, mes {obtener_mes(fecha_completa)} y año {obtener_anio(fecha_completa)}.")

if __name__ == "__main__":
    main()