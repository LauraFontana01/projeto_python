# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# D) Crie uma lista com 6 nomes, depois verifique se o nome ‘Pedro’ está nessa lista.

import os


os.system('cls')

# Título
print('=' * 80)
print('Verificação de nome "Pedro": ')
print('=' * 80)
print()

# Entrada 1
nomes_1 = ['Abigail', 'Bruno', 'Corbus', 'Demetrius', 'Elliot', 'Feiticeiro']
nomes_2 = ['Laura', 'Marnie', 'Nierre', 'Pedro', 'sr. Qi,', 'Robin']

# Verificação de nome na lista
print('=' * 80)
print(f'Lista 2: {nomes_1}')
print('-' * 80)
if 'Pedro' in nomes_1:
    print('O nome Pedro está na lista.')
else:
    print('O nome Pedro não está na lista.')
print('=' * 80)
print(f'Lista 1: {nomes_2}')
print('-' * 80)
if 'Pedro' in nomes_2:
    print('O nome Pedro está na lista.')
else:
    print('O nome Pedro não está na lista.')
print('=' * 80)