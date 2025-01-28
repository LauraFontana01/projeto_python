# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que imprima os valores no intervalo definidos pelo usuário.  Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

import os


os.system('cls')

inicio = int(input('Início do Intervalo: '))
fim = int(input('Fim do Intervalo: '))

for intervalo in range(inicio, fim+1):
    if intervalo==3:
        continue
    if intervalo ==5:
        continue
    if intervalo == 6:
        continue
    else:
        print(f'{intervalo}')