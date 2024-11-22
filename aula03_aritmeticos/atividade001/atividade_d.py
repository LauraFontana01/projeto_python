# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Implemente um programa que receba dois números e realize a divisão, formatando o resultado com quatro casas decimais.

import os

os.system('cls')

print('-'*70)
print('Eu sei realizar a divisão de dois números com resultado tendo quatro casas decimais! Dúvida?')
print('-'*70)

print()
print(' Vou te mostrar!')
print('-'*70)
dividendo = float(input('Entre com o dividendo: '))
divisor = float(input('Entre com o divisor: '))

quociente = dividendo / divisor

print('-'*70)
print(f'A divisão de {dividendo} ÷ {divisor} é: {quociente:.4f}') 
