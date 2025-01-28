# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Atividade 9 letra A -  Crie um programa que permita ao usuário
# inserir chaves e valores em um dicionário, garantindo que as chaves 
# sejam únicas. Após o cadastro, exiba o dicionário ordenado pelas 
# chaves.

import os


os.system('cls')

# Título 
print('-'*50)
print('Criando um Dicionário com 4 elementos!')
print('-'*50)


# Criação de uma caixa vazia "dict_1" onde você vai guardar 
# os nomes (chaves) e as informações (valores).
# Essa "caixa" é o que chamamos de dicionário em Python.
dict_1 = {}

# Iteração é como dizer: "Vamos fazer isso 4 vezes!",
#  onde usamos "for i in range(value)" . 
# A cada vez, ele vai pedir um nome (chave) e 
# uma informação (valor) para guardar no dicionário.
for i in range(4): # "i" significa iteração

    # Iterar as chaves, onde se repetir uma chave, vai dar erro.
    while True:
        key = input(f'Digite a {i + 1}ª chave: ').strip().capitalize()
        print('-'*50)

        # Condicionar chave "if key in dict"
        if key in dict_1:
            print('Erro! Insira uma chave única.')
            print('-'*50)
            print()
        else:
            break

    # Iterar valor - Ele pergunta: 
    # "Qual é a informação sobre essa coisa?" (exemplo: "Vermelho").
    # Depois, guarda o par nome + informação na caixa. Por exemplo:
    # "Carro": "Vermelho"
    value = input(f'Digie o {i + 1}º valor: ').strip().capitalize()
    print('-'*50)
    
    
    # Adicionar par chave-valor ao dict
    dict_1[key] = value 

# Ordenação por chave - Aqui, ele pega todos os pares guardados
# na caixa e organiza os nomes em ordem alfabética, 
# para ficar mais fácil de ler.
dict_ordenado = sorted(dict_1.items())

# Exibição - No final, ele mostra tudo que você colocou na caixa, 
# bonitinho e organizado.
print('-'*50)
for key, value in dict_ordenado:
    print(f'{key}: {value}')
print('-'*50)
print()
