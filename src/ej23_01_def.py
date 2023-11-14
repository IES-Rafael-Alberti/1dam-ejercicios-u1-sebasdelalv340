"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""

def obtener_username(email):
    username = email.split("@")
    return username

def main():
    email = input("Introduce tu correo electrónico: ")
    print(obtener_username(email)[0] + "@ceu.es")

if __name__ == "__main__":
    main()