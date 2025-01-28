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
#• Os múltiplos de 2, 3 e 4 - iteração desses números - (i % 2 == 0) or (i % 3 == 0) or (i % 4 == 0)
#• Lista reversa
#• O produto dos intervalos 5-6 por 11-12

import os


os.system('cls')

print('-'*50)
print('Intervalos e elementos em Lista!')
print('-'*50)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
multiplos = []

# Fatiamento da lista
intervalo1 = lista[0 : 9]
intervalo2 = lista[7 : 13]
pares = lista[1 : 15 : 2]
impares = lista[0 : 15 : 2]
reverse = lista[::-1]
intervalo3 = lista[4 : 6]
intervalo4 = lista[10 : 12]

for i in lista:
    if (i % 2 == 0 ) or (i % 3 == 0) or (i % 4 == 0):
        multiplos.append(i)

# Produto dos intervalos 3(5-6) e 4(11-12)
produto = [
    int3 * int4 
    for int3 in intervalo3
    for int4 in intervalo4
]

# Saída
print(f'Lista base: {lista}')
print('-'*50)
print(f'Intervalo entre 1 a 9: {intervalo1}')
print('-'*50)
print(f'Intervalo entre 8 a 13: {intervalo2}')
print('-'*50)
print(f'Números pares: {pares}')
print('-'*50)
print(f'Números Ímpares: {impares}')
print('-'*50)
print(f'Múltiplos de 2, 3 e 4: {multiplos}')
print('-'*50)
print(f'Lista inversa: {reverse}')
print('-'*50)
print(f'O produto dos intervalos 5-6 por 11-12: {produto}')
print('.'*50)
