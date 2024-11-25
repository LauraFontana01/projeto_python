# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 21/11/2024
# Estrutura de Dados
# O código remove um elemento de uma lista em um índice fornecido pelo usuário, verifica a validade do índice e exibe o elemento removido ou uma mensagem de erro, além da lista atualizada.

import os


os.system('cls')

# Inicializa uma lista de exemplo
lista_numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Solicita ao usuário para inserir um índice para remover o elemento
indice = int(input('Digite o índice do elemento a ser removido (0-9): '))

# Verifica se o índice está dentro do intervalo válido da lista
if 0 <= indice < len(lista_numeros):
    # Remove o elemento no índice especificado e exibe-o
    elemento_removido = lista_numeros.pop(indice)
    print(f'Elemento removido: {elemento_removido}')
else:
    print('Índice inválido!')

# Exibe a lista resultante
print('Lista após remoção:', lista_numeros)