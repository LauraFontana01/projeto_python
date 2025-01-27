# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/01/2025
# Crie uma função que receba uma lista de números. 
# Depois retorne duas listas com:
# os números pares, 
# os números ímpares, 
# a quantidade de números pares e a quantidade de números ímpares.

import os


os.system('cls')

# Primeiro passo: Definir função "def function(param)" 
def listar_numeros(numero):

    lista_par = []
    lista_impar = []

    # Verificação dos números pares e ímpares
    for n in lista:
        if n % 2 == 0:
            lista_par.append(n) # Append adiciona um item no final da lista
        else:
            lista_impar.append(n)

        # Contagem dos números nas listas - Len retorna o número de ocorrências de tal elemento
        quantidade_par = len(lista_par)
        quantidade_impar = len(lista_impar)

     # Retorna os valores feitos dentro da função
    return lista_par, lista_impar, quantidade_par, quantidade_impar

# Definindo a lista de números
lista = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Chamando a função
lista_par, lista_impar, quantidade_par, quantidade_impar = listar_numeros(lista)

# Saídas
print('Lista de números pares:', lista_par)
print('Quantidade de pares:', quantidade_par)
print('Lista de números ímpares', lista_impar)
print('Quantidade de ímpares:', quantidade_impar)

    