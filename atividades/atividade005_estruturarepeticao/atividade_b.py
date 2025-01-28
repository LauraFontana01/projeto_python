# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Evolua o programa anterior para um código que pergunte ao usuário qual o intervalo que ele deseja ver  impresso.

import os


os.system('cls')

print('-'*50)
print('Intervalo')
print('.'*50)

# Entrada de variáveis - Começo e fim de intervalo
inicio = int(input('Início de Intervalo: '))
fim = int(input('Final do Intervalo: '))

# Looping/Processamento entre intervalo, como proposto no enunciado
for numero in range(inicio, fim+1):
    print(f'{numero}')