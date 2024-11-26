# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# G) Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

print('-'*50)
print('Maior e menor número da Lista!')
print('-'*50)

lista = []

for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número: '))
    lista.append(numero)

print('.'*50)
print(f'Lista: {lista}')

listaordenada = lista.sort()

for j in range(len(lista)):
    print(f'{lista[j]}', end=' ')