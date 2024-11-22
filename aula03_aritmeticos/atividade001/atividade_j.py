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

base = float(input('Insira o valor da base: '))
altura = float(input('Insira a altura: '))
perimetro = 2*(base + altura)

print(f'O perímetro de um retângulo com base {base} e altura {altura} será igual a: {perimetro}')
