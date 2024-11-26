# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# E) Faça um programa que leia as vogais, depois mostre-as em ordem inversa.

import os


os.system('cls')

print('-'*50)
print('Inversão de vogais!')
print('-'*50)

lista = ['a', 'e', 'i', 'o', 'u']

vogais = lista[::-1]

print(f'Lista de vogais: {lista}')
print(f'Lista de vogais invertida: {vogais}')