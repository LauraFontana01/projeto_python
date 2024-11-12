# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que receba o nome completo de uma pessoa e, posteriormente, imprima esse nome separadamente.
# receba o nome completo de alguem e imprima esse 
# nome separadamente.

import os


os.system('cls')

print('-'*50)
print('Divisão de palavras na frase')
print('-'*50)

nome = 'Laura Fontana Ribeiro'

lista = nome.split() # split(sep): Divide a string em substrings com base no separador especificado e retorna uma lista das substrings resultantes.

print(lista)



