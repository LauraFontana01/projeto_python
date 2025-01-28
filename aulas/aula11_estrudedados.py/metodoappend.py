# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 21/11/2024
# Estrutura de Dados
# O código solicita ao usuário para inserir três números, adiciona-os a uma lista e, a cada inserção, permite que o usuário busque um número na lista, informando se ele está presente ou não.
# append: inserir elementos dentro de uma lista, item a item

import os


os.system('cls')

# Inicializa uma lista vazia
lista_numeros = []

# Pede ao usuário para inserir três números
for i in range(3):
    numero = int(input('Digite um número: '))

    # Adiciona o número à lista
    lista_numeros.append(numero)

    print(f'Lista gerada: {lista_numeros}')
    # Verifica se o número inserido está na lista e exibe uma mensagem correspondente
    print('-'*50)
    numero_verificar = int(input('Número para busca: '))
    print('-'*50)

    if numero_verificar in lista_numeros:
        print(f'O número {numero_verificar} está na lista!')
    else: 
        print(f'O número {numero_verificar} não está na lista!')