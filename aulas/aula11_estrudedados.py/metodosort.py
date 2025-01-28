# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código cria uma lista de números fornecida pelo usuário, ordena a lista em ordem ascendente ou descendente conforme escolhido, ou exibe uma mensagem de erro caso a opção seja inválida.

import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de string
numeros_str = entrada.split()

# Converte a lista  de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para escolher a ordem de classificação
ordem = input(
    "Digite 'asc' para ordem ascendente ou 'desc'"
    "para ordem decrescente: ").strip().lower()

# Verifica a escolha do usuário e ordena a lista de acordo
if ordem == 'asc':
    numeros.sort()
    print(f'Lista ordenada em ordem ascendente: {numeros}')
elif ordem == 'desc':
    numeros.sort(reverse=True)
    print(f'Lista ordenada em ordem decrescente: {numeros}')
else:
    print('Opção inválida! A lista não foi ordenada!')

# Exibe a lista fornecida para referência
print('Lista fornecida: ', numeros)