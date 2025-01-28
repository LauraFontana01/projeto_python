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
print('Brincadeira com Vogais')
print('-'*50)

# Lista de vogais 
lista_vogais = ['a', 'e', 'i', 'o', 'u']

# Inversão da lista
vogais = lista_vogais[::-1]

print(f'Lista original: {lista_vogais}')
print(f'Lista Invertida: {vogais}')

