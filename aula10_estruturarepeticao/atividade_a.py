# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que imprima os números no intervalo entre 1 e 100. Os números devem ser apresentados na horizontal.

import os


os.system('cls')

print('-'*50)
print('Números no Intervalo')
print('.'*50)

# Looping entre 1 a 100 + Saída
for numero in range(1, 101):
    print(f'{numero}', end = ' - ')
    
