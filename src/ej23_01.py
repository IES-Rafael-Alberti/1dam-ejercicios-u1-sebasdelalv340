"""Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es."""

def main():

    email = input("Introduce tu correo electrónico: ")

    username = email.split("@")[0]
    print(username + "@ceu.es")

if __name__ == "__main__":
    main()