# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que imprima os números pares entre 0 e 100.

import os


os.system('cls')

print('-'*50)
print('Números pares de 1 a 100')
print('.'*50)

# Looping números pares 0 a 100
for numero in range(0, 101, 2):
    print(f'{numero}', end = ' - ')