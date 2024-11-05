# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que leia uma frase e depois exiba na tela:
# A frase em minúsculas, a frase em maiúsculas, a quantidade de caracteres na frase e quantas letras tem a 2ª palavra na frase.

import os


os.system('cls')

print('~'*50)
print('Contagem de Caracteres!')
print('~'*50)

frase = 'Eu AMO Pizza de Pepperonni!'

minusculas = frase.lower()
print(f'Frase original: {frase}')
print(f'Frase nova: {minusculas}')
print('~'*50)

maiusculas = frase.upper()
print(f'Frase original: ')
print(f'Frase nome: {maiusculas}')
print('~'*50)

frase = "Eu AMO Pizza de Pepperonni!"
quantidade_caracteres = len(frase)
print(f'A frase {frase} \ncontém {quantidade_caracteres}!')
print('~'*50)

frase2 = "AMO"
quantidade_caracteres2 = len(frase2)
print(f'A 2ª frase "{frase2}" \ncontém {quantidade_caracteres2}')
print('~'*50)
