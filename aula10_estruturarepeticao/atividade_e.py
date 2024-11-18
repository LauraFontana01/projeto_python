# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Faça um programa que some a quantidade de números pares encontrados no intervalo entre 0 e 100.

import os


os.system('cls')

print('-'*50)
print('Soma de números pares entre 0 e 100')
print('.'*50)

# Entrada de contador
soma = 0 

# Iteração no intervalo de 0 a 100
for numero in range(0, 101):
    # Verificação de número par
    if numero % 2 == 0:
        soma += 1 # soma = soma + 1

print(f'Números pares encontrados: {soma}')
print()