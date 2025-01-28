# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# F) Faça um programa que leia 5 nomes, 
# depois imprima estes nomes com seus respectivos índices. 
# enumerate - retorna partes de índice e valor durante a iteração

import os


os.system('cls')

print('-'*50)
print('Índices')
print('-'*50)

# Cria-se uma entrada de lista para receber os 5 nomes
lista_nomes = []

# Iteração dos 5 nomes
for i in range (1, 6):
    nome = input(f'Digite o {i}º nome: ')
    print('-'*50)

    # Inserção da Lista
    lista_nomes.append(nome)
print('-'*50)

# Enumeração do Índice
print('-'*50)
for indice, nome in enumerate(lista_nomes):
    print(f'Índice: {indice} | Nome: {nome}')