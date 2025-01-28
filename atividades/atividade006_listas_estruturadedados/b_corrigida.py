# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# B) Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

numeros = input('Digite 5 números inteiros separados por espaço: ')

soma = 0
for numero in numeros:
    numero = int(numero)
    soma += numero

print('Números: ', end= '')
for numero in numeros:
    print(numero, end='')

print()
print(f'A soma dos números é: {soma}')