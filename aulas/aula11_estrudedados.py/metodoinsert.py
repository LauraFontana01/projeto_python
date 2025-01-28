# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 21/11/2024
# Estrutura de Dados
# O código solicita ao usuário uma posição e um elemento para inserir em uma lista, verifica se a posição é válida e, se for,
#  insere o elemento na lista e exibe a lista atualizada. Caso a posição seja inválida, exibe uma mensagem de erro.

import os


os.system('cls')

# Lista original 
lista = [1, 2, 3, 4]

# Pedindo ao usuário pra fornecer a posição e o elemento a ser inserido
posicao = int(input('Posição onde deseja inserir o elemento: '))
elemento = input('Elemento a ser inserido: ')

# Verificando se a posição fornecida pelo usuário é válida
if posicao >= 0 and posicao <= len(lista):
    # Inserindo o elemento na lista na posição especificada pelo usuário
    lista.insert(posicao, elemento)
    print('Lista após a inserção:', lista)
else:
    print(f'Posição fora do intervalo 0, {len(lista)}')