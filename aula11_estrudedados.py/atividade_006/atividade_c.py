# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# C) Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
#• O intervalo de 1 até 9
#• O intervalo de 8 até 13
#• Os números pares
#• Os números ímpares
#• Os múltiplos de 2, 3 e 4
#• Lista reversa
#• O produto dos intervalos 5-6 por 11-12


import os


os.system('cls')

print('-'*50)
print()
print('Lista Númerica')
print()
print('.'*50)

# Entrada 
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
multiplos = []

# Fatiamento da lista
intervalo_1 = lista[0 : 9]
intervalo_2 = lista[7 : 13]
pares = lista[1 : 15 : 2]
impares = lista[0 : 15 : 2]
reversa = lista[::-1]
intervalo_3 = lista[4 : 6]
intervalo_4 = lista[10 : 12]

# Iteração lista
for i in lista:
    
    # Condição múltiplo de 2, 3 e 4
    if (i % 2 == 0) or (i % 3 == 0) or (i % 4 == 0):
        multiplos.append(i)

# Produto dos intervalos 3 e 4
produto = [
    a * b
    for a in intervalo_3
    for b in intervalo_4
]

# Saída
print(f'Lista inicial: {lista}')
print('-' * 50)
print(f'Intervalo de 1 a 9: {intervalo_1}')
print('-' * 50)
print(f'Intervalo de 8 a 13: {intervalo_2}')
print('-' * 50)
print(f'Números pares: {pares}')
print('-' * 50)
print(f'Números ímpares: {impares}')
print('-' * 50)
print(f'Múltiplos de 2, 3 e 4: {multiplos}')
print('-' * 50)
print(f'Lista revertida: {reversa}')
print('-' * 50)
print(f'Produto dos intervalos 5-6 por 11-12: {produto}')
print('=' * 50)
print()
