

import os


os.system('cls')

print('-'*50)
print('Estrutura de Dados: Listas [ ]')
print('-'*50)

lista_mista = ['a', 'b', 3, 'John', 'e', 500, 'g', 'h']

# Fatia o 1º elemento
lista_fatiada1 = lista_mista[0]
# Fatia todos os elementos 
lista_fatiada2 = lista_mista[0:]
# Fatia os elementos do índice 0 até o índice até o índice 5
lista_fatiada3 = lista_mista[0:6]
# Fatia os elementos do índice 0 até o índice 6 de 2 em 2
lista_fatiada4 = lista_mista[0:6:2]
# Fatia os elementos da direita pra esquerda
lista_fatiada5 = lista_mista[::-1]

print(f'Fatiando uma lista: {lista_fatiada1}\n')
print(f'Fatiando uma lista: {lista_fatiada2}\n')
print(f'Fatiando uma lista: {lista_fatiada3}\n')
print(f'Fatiando uma lista: {lista_fatiada4}\n')
print(f'Fatiando uma lista: {lista_fatiada5}\n')

print('-'*50)
print('Fim do programa!')
print('-'*50)