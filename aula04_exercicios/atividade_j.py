# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Atividade001 -  Operadores Aritmeticos / Elabore um programa que peça as dimensões de um retângulo e calcule seu perímetro.

import os

os.system('cls')

print('-'*70)
print('Eu consigo calcular o perímetro de um retângulo! Gostaria de testar?')
print('-'*70)

b = float(input('Insira o valor da base: '))
a = float(input('Insira a altura: '))
p = 2*(b + a)

print(f'O perímetro de um retângulo com base {b} e altura {a} será igual a: {p}')
