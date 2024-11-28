# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# F) Faça um programa que gere 10 números aleatórios. Após gerar esses números, crie duas listas novas com ordenação ascendente e descendente.

import os
import random


os.system('cls')

# Título
print('=' * 70)
print('Lista aleatória de 10 números (1-100), ordem crescente e decrescente:')
print('=' * 70)
print()

# Entrada
lista_aleatoria = random.sample(range(1, 101), 10)

# Ordenação lista
lista_crescente = sorted(lista_aleatoria)
lista_decrescente = sorted(lista_aleatoria, reverse = True)

# Saída
print('=' * 70)
print(f'Lista Inicial: {lista_aleatoria}')
print('-' * 70)
print(f'Lista Crescente: {lista_crescente}')
print('-' * 70)
print(f'Lista Decrescente: {lista_decrescente}')
print('=' * 70)
print()