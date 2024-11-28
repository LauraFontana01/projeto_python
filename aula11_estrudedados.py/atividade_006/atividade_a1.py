# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# A) Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.

import os


os.system('cls')

print('-'*50)
print('Inserção de valores na lista')
print('-'*50)

# Lista
lista = [1, 2, 3, 5, 6]

print(f'Lista original: {lista}')
# Inserção de valor
lista.append(4)

# Ordenar lista
lista.sort()

# Saída
print(f'Lista com inserção: {lista}')
print('-'*50)
