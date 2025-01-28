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
print('Soma de valores de uma lista')
print('-'*50)

lista = [2, 4, 6, 8, 10]
print(f'Lista: {lista}')
print('-'*50)
# Flag - variavel contador
soma = 0

# Iteração dos 5 números - looping "for" ou "while" - i é o elemento e após vem o grupo, que no caso é lista
for numeros in lista:
    soma += numeros

# Saída
print(f'Soma dos valores da lista: {soma}')
