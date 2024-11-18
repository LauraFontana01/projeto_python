# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário.

import os


os.system('cls')

print('-'*50)
print('Números primos em um intervalo')
print('.'*50)

# Entrada de intervalo pelo usuário
inicio = int(input('Início do Intervalo: '))
fim = int(input('Fim do Intervalo: '))

# Processamento dos intervalos
for intervalo in range(inicio, fim + 1):
    # Condição de i