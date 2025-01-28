# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 04/11/2024
# Biblioteca Math
# Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
# Calcule as raízes da equação do 2º grau seguindo a fórmula:
# Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

import os
import math

os.system('cls')

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
c = int(input('Insira o valor de C: '))

delta = (b ** 2) - (4 * a * c)


if delta < 0:
    print('As raízes são complexas')
else:
    raizdelta = math.sqrt(delta)

    x1 = (-b + raizdelta)  / 2*a
    x2 = (-b - raizdelta)  / 2*a



print(f'As raízes são: {x1} e {x2}')