# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 28/01/2025

import os


os.system('cls')

# Definindo uma função para empacotar
def empacotar(*lista_numeros):
    print(f'Empacotados: {lista_numeros}')
    for i in lista_numeros:
        print(f'Empacotado: {i}')

# Invocando a função empacotar
empacotar(1, 2, 3, 4, 5)

# Desempacotando (lista)
def desempacotar(a, b, c, d, e):
    print('Desempacotar:')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')
    print(f'e = {e}')

# Invocando a função desempacotar
lista_numeros = [1, 2, 3, 4, 5] # lista
desempacotar(*lista_numeros) # * args

# Packing Dicionário 
def empacotar_dicionario(**dados_dicionario): # ** kwargs
    print(f'Dados do dicionário: {dados_dicionario}')
    for k, v in dados_dicionario.items():
        print(f'Chave: {k}, valor: {v}')

print('-'*50)
print('---Dicionário')
empacotar_dicionario(nome = 'Juquinha', idade = 70, peso = 70.5)

# Unpacking Dicionário
print('-'*50)
def desempacotar_dicionario(nome, idade, peso):
    print(f'Nome = {nome}')
    print(f'idade = {idade}')
    print(f'Peso = {peso}')

dicionario = dict(nome = 'Maria', idade = 70, peso = 70.5)
desempacotar_dicionario(**dicionario)
print()