# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana Ribeiro
# Professor: Sebastião Marcos
# Data: 13/01/2025

import os


os.system('cls')

print('-'*50)
print('Estrutura de Dados: Dicionário') # dict => {}
print('-'*50)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# Atribuindo Valores
compras['id'] = 1
compras['item']= 'Caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sir Sherlock Holmes'
pessoas['endereco'] = 'Baker Street'
pessoas['numero'] = '2218'
pessoas['cidade'] = 'Londres'
pessoas['pais'] =  'Inglaterra'

cores['red'] = 'Vermelho'
cores['green'] = 'Verde'
cores['blue'] = 'Azul'

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogênio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# Saída Simples
print(f'Minhas compras: {compras}')
print(f'Detetives: {pessoas}')
print(f'Cor RGB: {cores}')
print(f'Tabela Períodica: {elementos}')
print(f'Listagem de números: {numeros}')
print()
print('-'*50)