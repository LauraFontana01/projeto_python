# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# B) Faça um programa que preencha uma lista com 50 números aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.

import os

import random

os.system('cls')

# Título
print('=' * 220)
print('Lista de 1 a 100 gerada aleatoriamente e fatiada em 5 listas menores:')
print('=' * 220)
print()

# Entrada
lista = random.sample(range(1, 101), 50)

# Fatiamento em 5 listas
for i in range(len(lista)):
    lista_1 = lista[:10]
    lista_2 = lista[10:20]
    lista_3 = lista[20:30]
    lista_4 = lista[30:40]
    lista_5 = lista[40:50]


# Saída
print('=' * 220)
print(f'Lista Inicial: {lista}')
print('-' * 220)
print(f'Lista 1: {lista_1}')
print('-' * 220)
print(f'Lista 2: {lista_2}')
print('-' * 220)
print(f'Lista 3: {lista_3}')
print('-' * 220)
print(f'Lista 4: {lista_4}')
print('-' * 220)
print(f'Lista 5: {lista_5}')
print('=' * 220)
print()