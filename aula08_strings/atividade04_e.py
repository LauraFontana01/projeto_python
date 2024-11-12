# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que receba uma frase e, em seguida, mostre quantas vezes as vogais foram utilizadas.

import os


os.system('cls')

print('~'*50)
print('Brincadeira das Vogais!')
print('~'*50)

frase = input('Digite uma frase: ').lower()

contagem_a = frase.count('a')          # count(substring): retorna o número de ocorrências da substring na string
contagem_e = frase.count('e')
contagem_i = frase.count('i')
contagem_o = frase.count('o')
contagem_u = frase.count('u')

todas = contagem_a + contagem_e + contagem_i + contagem_o + contagem_u 
print(f'As vogais aparecem {todas} vezes!')