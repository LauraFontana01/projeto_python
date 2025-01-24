# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Crie um programa que trabalhe com um dicionário de uma pessoa contendo:
#  nome, idade, peso e altura. 
# O programa deve: Listar as chaves e os valores usando um laço de repetição.
# Permitir excluir o item "peso" e garantir que ele seja removido.
# Exibir novamente o nome e a altura da pessoa, mostrando o dicionário atualizado.

import os

os.system('cls')

dados = {'nome': 'john', 'idade': '40' , 'peso': '80', 'altura': '1.70'}

for keys, values in dados.items():
    print(f'{keys}: {values}')



del dados['peso']

print('=' * 70)

for keys, values in dados.items():
    print(f'{keys}: {values}')