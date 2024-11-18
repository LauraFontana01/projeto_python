# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que imprima os números no intervalo entre 1 e 10 em ordem inversa.

import os


os.system('cls')

print('-'*50)
print('Números em um Intervalo')
print('.'*50)

# Looping entre 10 e 1, sendo sequência inversa
for numero in range(10, 0, -1):
    print(f'{numero}')