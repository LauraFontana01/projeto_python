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

nome = input('Digite seu nome: ').capitalize()
nomedomeio = input('Digite seu nome do meio: ').capitalize()
sobrenome = input('Digite seu sobrenome: ').capitalize()

nomecompleto = nome + ' ' + nomedomeio +' ' + sobrenome

print('-'*50)
print(f'Seu nome completo é {nomecompleto}!')

