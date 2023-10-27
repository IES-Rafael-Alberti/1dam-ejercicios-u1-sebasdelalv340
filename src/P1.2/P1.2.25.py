"""Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter."""

def main():

    fecha_completa = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
    
    #dia = fecha_completa[:2]
    #mes = fecha_completa[3:5]
    #año = fecha_completa[6:]

    #print(f"El día {dia}, mes {mes} y año {año}.")

    lista = fecha_completa.split("/")
    
    dia = lista[0]
    mes = lista[1]
    año = lista[2]
    print(f"El día {dia}, mes {mes} y año {año}.")

if __name__ == "__main__":
    main()