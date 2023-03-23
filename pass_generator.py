# Genera una contraseña aleatoria a partir de una longitud determinada de caracteres dada por el usuario.

import random
import string

def pass_generator(length, allow_repeats):
    if allow_repeats == 's':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(characters, length))
    return password


def run():
    print('Para contraseñas más fuertes considere una longitud más amplia 💡\n')
    max_length = 40
    length = int(input('Ingrese la longitud deseada de la contraseña: '))
    length = max(0, min(length, max_length))
    allow_repeats = input('¿Desea que su contraseña permita caracteres repetidos? (S/N): ').lower()
    password = pass_generator(length, allow_repeats)
    print('Contraseña generada con éxito 🔒\n')
    print('Su contraseña es: ' + password)


if __name__ == '__main__':
    run()
