# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código percorre uma lista de números utilizando enumerate(), que adiciona um índice a cada elemento da lista.
# Para cada elemento, o código exibe o índice e o número, e calcula a soma total dos números. No final, exibe a soma dos números e uma mensagem de término.
import os


os.system('cls')

print('-'*50)
print('Saída com For...Enumerate()')
print('-'*50)

soma = 0

# Criando uma lista
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Percorrendo a lista com o enumerate(), o comando enumerate adiciona
# um índice para cada valor de nossa lista! 
# Start opcional, para não começar no índice 0
# enumerate(listaNumeros, start = 1)

# Para cada número dentro da lista de números, enumere com um índice
for indice, numero in enumerate(lista_numeros):
    soma += numero # soma os números
    print(f'Índice: {indice} = Número: {numero}')

print('-'*50)
print(f'A soma de todos os números é: {soma}')
print('Fim do programa!')
print('-'*50)