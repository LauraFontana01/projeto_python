# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# B) Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.

import os


os.system('cls')

print('-'*50)
print('Soma da lista!')
print('-'*50)

lista = [2, 4, 6, 8, 10]

# Variavel para a soma/ Flag
soma = 0

# Looping de soma de cada elemento na lista
for numero in lista:
    soma += numero

print(f'A soma dos valores inteiros da lista {lista} é: {soma}')