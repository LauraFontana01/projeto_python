# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Desenvolva um programa que peça um número qualquer e calcule o dobro e o triplo desse número.

import os

os.system('cls')

print('-'*70)
print('Eu consigo calcular o dobro e o triplo de qualquer número inteiro! Tenta ai!')
print('-'*70)

# Entrada
n1 = int(input('Digite um número: '))

# Processamento
dobro = n1 * 2
triplo = n1 * 3

# Saida
print('-'*70)
print(f'O dobro é: {dobro}')
print(f'Já o sucessor é: {triplo}')
print('-'*70)

