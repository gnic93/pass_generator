# Genera una contraseña aleatoria a partir de una longitud determinada de caracteres dada por el usuario.

import random
import string

def pass_generator(length, allow_repeats):
    if allow_repeats:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.sample(characters, length))
    return password


def main():
    print('💡 Para contraseñas más fuertes considere una longitud más amplia\n')
    max_length = 94
    while True:
        try:
            length = int(input('Ingrese longitud de caracteres: '))
            if length < 8 or length > max_length:
                raise ValueError(f"La longitud de la contraseña debe estar entre 8 y {max_length}.")
            break
        except ValueError:
            print("Debe ingresar un número entero válido para la longitud de la contraseña.")
    while True:
        allow_repeats = input('¿Desea que su contraseña permita caracteres repetidos? (S/N): ').lower()
        if allow_repeats in {'s', 'n'}:
            allow_repeats = allow_repeats == 's'
            break
        else:
            print("Debe responder 's' o 'n' para permitir o no permitir caracteres repetidos en la contraseña.")
            
    password = pass_generator(length, allow_repeats)
    print('\n')
    print('🔒 Contraseña generada con éxito')
    print(f'Su contraseña es: {password}')


if __name__ == '__main__':
    main()
