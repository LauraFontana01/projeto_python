# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que receba o nome completo de uma pessoa e, em seguida, mostre o primeiro e o último nome.

import os


os.system('cls')

print('~'*50)
print('Brincadeira com Nomes e Sobrenomes!')
print('.'*50)

nome_completo = input('Coloque seu nome: ').capitalize().strip()

lista = nome_completo.split()
primeiro = lista[0:1]
ultimo = lista[-1:]

print(f'Seu primeiro nome é {primeiro} e seu último é {ultimo}!')