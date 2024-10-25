# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Faça um programa que receba um número inteiro e exiba seu sucessor e antecessor.

import os

os.system('cls')

print('-'*70)
print('Eu consigo calcular o sucessor e o antecessor de qualquer número inteiro! Tenta ai')
print('-'*70)

# Entrada
n1 = int(input('Digite um número: '))

# Processamento
antecessor = n1 - 1
sucessor = n1 + 1

# Saida
print('-'*70)
print(f'O número antecessor é: {antecessor}')
print(f'Já o sucessor é: {sucessor}')
print('-'*70)
