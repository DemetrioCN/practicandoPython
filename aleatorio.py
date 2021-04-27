# -*- coding: utf-8 -*-
import random

def run(inicio, final):
    number_found = False
    random_number = random.randint(inicio, final)

    while not number_found:
        number = int(input('Intenta un número：'))

        if number == random_number:
            print('Felicidades. Encontraste el número')
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    inicio = int(input('Ingrese el numero inicial: '))
    final = int(input('Ingrese el numero final: '))

    run(inicio, final)