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
print('Inserção de número faltante em lista!')
print('-'*50)

lista_numeros = [1, 2, 3, 5, 6]

print(f'Lista original: {lista_numeros}')
print('.'*50)

lista_numeros.insert(3, 4) # Inseriu o nº 4 no índice 3
print(f'Lista modificada: {lista_numeros}')
