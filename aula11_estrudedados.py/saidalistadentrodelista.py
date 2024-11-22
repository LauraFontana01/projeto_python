# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código exibe uma estrutura de jogo da velha representada como uma lista de listas, acessa elementos específicos manualmente e utiliza loops para percorrer
#  e imprimir todos os elementos organizados em linhas e colunas.

import os


os.system('cls')

print('-'*50)
print('Varrendo Listas dentro de Listas')
print('.'*50)

# X O X
# X X O
# O O O

# Similar a um array de 3 Dimensões
jogo_velha = [
                # 0   1   2 
                ['X', 'O', 'X'], # 0
                ['X', 'O', 'X'], # 1
                ['O', 'O', 'O']  # 2
]

print(jogo_velha)
print('-'*50)

# Pegando manualmente os valores
print(f'Na linha 1 coluna 1, existe um: {jogo_velha[1][1]}')
print(f'Na linha 0 coluna 2, existe um: {jogo_velha[0][2]}')

print()
# Varrendo com for range
for linha in range(0, len(jogo_velha)):
    for coluna in range(0, len(jogo_velha)):
        print(jogo_velha[linha][coluna], end=' ')
    print()
print()