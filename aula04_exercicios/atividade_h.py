# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Implemente um programa que receba um número inteiro e imprima sua tabuada de multiplicação.

import os

os.system('cls')

print('-'*70)
print('Me diga um número inteiro e eu te mostro a tabuada de multiplicação dele!')
print('-'*70)

# Entrada
n = int(input('Digite um número: '))

# Processamento
vezes1 = n * 1
vezes2 = n * 2
vezes3 = n * 3
vezes4 = n * 4
vezes5 = n * 5
vezes6 = n * 6
vezes7 = n * 7
vezes8 = n * 8
vezes9 = n * 9
vezes10 = n * 10
resultado = vezes1, vezes2, vezes3, vezes4, vezes5, vezes6, vezes7, vezes8, vezes9, vezes10
# Saida
print(f'A tabuada de {n} é igual a {resultado}')
print('-')