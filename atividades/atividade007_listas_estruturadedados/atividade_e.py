# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# E) Faça um programa que receba 7 números inteiros. Depois quebre essa lista em: lista de pares e lista de ímpares. 

import os


os.system('cls')

# Título
print('=' * 70)
print('Lista de 7 números e separação em pares ou ímpares:')
print('=' * 70)
print()

# Entrada
lista = []
lista_par = []
lista_impar = []

# Iteração 7 números
print('-' * 70)
for i in range (1, 8):
    numero = int(input(f'Digite o {i}º valor: '))
    print('-' * 70)

    # Inserção de valores na lista
    lista.append(numero)
print()

# Condição para par ou ímpar
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista_par.append(lista[i])
    else:
        lista_impar.append(lista[i])

# Saída
print('=' * 70)
print(f'Lista Inicial: {lista}')
print('-' * 70)
print(f'Lista Par: {lista_par}')
print('-' * 70)
print(f'Lista Ímpar: {lista_impar}')
print('=' * 70)
print()