"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""

def obtener_imc(peso, estatura):
    indice = peso / (estatura ** 2)
    return indice

def main():
    peso = float(input("Introduce tu peso (en kg): "))
    estatura = float(input("Introduce tu estatura (en metros): "))
    print("Tu índice de masa corporal es {:.2f}".format(obtener_imc(peso, estatura)))

if __name__ == "__main__":
    main()    