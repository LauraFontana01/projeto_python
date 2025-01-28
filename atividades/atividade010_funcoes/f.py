# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/01/2025
# Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade 
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave 
# e valor utilizando como base essas duas listas. 
# Depois, seu programa deverá imprimir esse dicionário utilizando 
# uma estrutura de repetição for.

import os


os.system('cls')

lista_livre = []
dicio = {}

def listas(lista_1, lista_2):

    nome = input('Insira o nome: ')
    peso = float(input('Insira seu peso: '))
    idade = int(input('Insira sua idade: '))

    lista_1 = [nome, peso, idade ]
    lista_2 = ['John', 40, 18]

    return {'Nome': nome, 'Peso': peso, 'Idade': idade}