# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código cria uma lista de números fornecida pelo usuário, conta quantas vezes um número específico aparece nela e exibe a contagem ou uma mensagem de ausência.
# sort ordena / reverse inverte

import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteiros
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para inserir o número fornecido aparece na lista
numero_para_contar = int(input('Digite o número que deseja contar: '))

# Conta o número de vezes que o número fornecido aparece na lista
contagem = numeros.count(numero_para_contar)

if contagem > 0:
    print(f'O número {numero_para_contar} aparece {contagem} vezes na lista!')
else:
    print(f'O número {numero_para_contar} não aparece na lista!')

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')