# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que solicite separadamente o nome, o nome do meio e o sobrenome de uma pessoa. Em seguida, imprima o nome completo.
# 1 o nome, 2 o nome do meio e o 3 sobrenome de uma pessoa
# Em seguida, imprima o nome completo.

import os


os.system('cls')

print('.'*50)
print('Seu nome completo')
print('~'*50)

nome = input('Insira seu nome: ').capitalize()
nomedomeio = input('Insira seu nome do meio: ').capitalize()
sobrenome = input('Insira seu sobrenome: ').capitalize()

nome_completo = nome +' '+ nomedomeio +'' + sobrenome

print(f'Seu nome é: {nome_completo}')


