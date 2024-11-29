# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/11/2024

import os


os.system('cls')

nomes = ['Laura', 'Heloísa', 'Mirna', 'Ana']

for indice, nome in enumerate(nomes):
    # Cria uma tupla contendo o índice e o nome da pessoa atual
    minha_tupla = (indice, nome)
    # A variável minha_tupla é utilizada para acessar o índice
    #e o nome armazenados na tupla. Mas posso acessar diretamente
    # os elementos 'índice' e 'nome'
    print(f'O nome "{minha_tupla[1]}", posição {minha_tupla[0]} da lista.')
    print(f'O nome "{nome}", posição {indice} da lista.')
    print('-'*50)