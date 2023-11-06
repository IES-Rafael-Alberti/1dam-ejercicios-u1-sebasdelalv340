"""Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera."""

def primera_mayuscula(nombre_completo):
    return nombre_completo.title()

def todo_mayuscula(nombre_completo):
    return nombre_completo.upper()

def todo_minuscula(nombre_completo):
    return nombre_completo.lower()

def main():
    nombre_completo = input("Introduzca su nombre completo: ")

    print(primera_mayuscula(nombre_completo))
    print(todo_mayuscula(nombre_completo))
    print(todo_minuscula(nombre_completo))

if __name__ == "__main__":
    main()