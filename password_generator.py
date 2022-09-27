import random

# Ejecucion de la funcion para generar el password.

print("Hola Quiero Ayudarte Con la Seguridad de Tus Contraseñas.")
print("Te Ayudare a Generar Contraseñas Seguras.")

# Declaro la funcion.
def password_generator():
    # Declaro la lista de caracteres.
    characters = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&/())========??¡*]['
    # Declaro la variable que va a contener el password.
    password = ''
    # Declaro la variable que va a contener el numero de caracteres.
    length = int(input('Cuantos caracteres quieres que tenga tu password? '))
    # Declaro la variable que va a contener el numero de caracteres.
    for i in range(length):
        password += random.choice(characters)
    # Retorno el password.
    return password

# Ejecucion de la funcion para generar el password.
def run():
    password = password_generator()
    print('Te Sugiero este password: ' + password)
    print('Para que sea seguro, te recomendamos que lo cambies.')
    print('Gracias por usarme. Adios.')

if __name__ == '__main__':
    run()
