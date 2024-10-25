# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Desenvolva um programa que solicite um valor em reais e calcule quantos dólares podem ser comprados com esse valor.

import os

os.system('cls')

print('-'*70)
print(' Calculadora de Dólar e Real')
print('-'*70)

reais = float(input('Insira quaquer valor em reais: '))

dolar = reais * 5.71

print(f'O valor {reais} real/reais será {dolar} dólar/dólares')
print('-'*70)