# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# G) Ler uma lista com 10 números, depois apresente o maior e o menor número da lista

import os


os.system('cls')

# Entrada de título
print('-'*50)
print('Lista com números: Qual o menor e qual o maior?')
print('-'*50)

# Lista onde receberá os números
lista = []

# Loop para receber os números e adiciona-los na lista
for i in range(1, 11):
    numero = int(input(f'Digite o {i}º número: '))
    lista.append(numero)

print('.'*50)
print(f'Lista: {lista}')

# Ordenação (ordem) dos números e fatiamento do menor e maior número
lista.sort()
menor_numero = lista[0]
maior_numero = lista[-1]


# Saída
print('=' * 70)
print(f'Lista ordenada: {lista}')
print('-' * 70)
print(f'O menor número da lista é: {menor_numero}')
print('-' * 70)
print(f'O maior número da lista é: {maior_numero}')
print('=' * 70)
print()


