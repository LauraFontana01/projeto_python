# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código cria uma lista de números fornecida pelo usuário, permite copiar a lista conforme a escolha do usuário e exibe a cópia ou mantém apenas a lista original.


import os


os.system('cls')

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de strings
numeros_str = entrada.split()

# Converte a lista de strings em uma lista de inteios
numeros = []
for num_str in numeros_str:
    numeros.append(int(num_str))

# Solicita ao usuário para decidir se deseja criar uma cópia da lista
escolha = input('Deseja criar uma cópia? (s/n): ').strip().lower()

# Verifica a escolha do usuário e cria uma cópia da lista se a resposta for 's'
if escolha == 's':
    lista_copiada = numeros.copy()
    print(f'Cópia da lista: {lista_copiada}')
else:
    print('A lista não foi copiada!')

# Exibe a lista fornecida para referência
print(f'Lista fornecida: {numeros}')