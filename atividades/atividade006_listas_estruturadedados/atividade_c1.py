# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# C) Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
#1• O intervalo de 1 até 9
#2• O intervalo de 8 até 13
#3• Os números pares
#4• Os números ímpares
#7• Os múltiplos de 2, 3 e 4 - iteração desses números - (i % 2 == 0) or (i % 3 == 0) or (i % 4 == 0) / cria-se uma condição if else após o for
#5• Lista reversa
#6• O produto dos intervalos 5-6 por 11-12

import os


os.system('cls')

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(f'Lista original: {lista}')

multiplos = []

# Condições
intervalo1 = lista[0 : 9]
intervalo2 = lista[7 : 13]
pares = lista[1::2]
impar = lista[0::2]
reverse = lista[::-1]

# Condição Múltiplos
for numeros in lista:
    if(numeros%2==0) or (numeros%3==0) or (numeros%4==0):
        multiplos.append(numeros)

# Condição Produto
intervalo3 = lista[4 : 6]
intervalo4 = lista[10 : 12]

produto = [
    int3 * int4 
    for int3 in intervalo3
    for int4 in intervalo4
]

# Saída
print('.'*50)
print(f'Intervalo de 1 a 9: {intervalo1}')
print('.'*50)
print(f'Intervalo de 8 a 13: {intervalo2}')
print('.'*50)
print(f'Números pares na lista: {pares}')
print('.'*50)
print(f'Números ímpares na lista: {impar}')
print('.'*50)
print(f'Lista reversa: {reverse}')
print('.'*50)
print(f'Múltiplos de 2, 3 e 4: {multiplos}')
print('.'*50)
print(f'Produto dos intervalos 5-6 e 11-12: {produto}')
print('.'*50)


