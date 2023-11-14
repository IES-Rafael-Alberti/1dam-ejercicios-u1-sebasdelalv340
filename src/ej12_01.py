"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""

peso = input("Introduce tu peso (en kg): ")
estatura = input("Introduce tu estatura (en metros): ")

indice = int(peso) / (float(estatura) ** 2)

print("Tu índice de masa corporal es {:.2f}".format(indice))