# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Estrutura de Dados
# O código solicita os nomes de 5 alunos, armazena-os em uma lista e os imprime, com uma tentativa de adicionar uma quebra de linha após o quarto nome.

import os


os.system('cls')

print('-'*50)
print('Saída com For')
print('-'*50)

# Criando uma lista
lista_alunos = []

for c in range (0, 5):
    nome = str(input('Entre com o nome do aluno: '))

    # Guardando em uma lista
    lista_alunos.append(nome)

print()
print('Impressão dos nomes de alunos: ')

# Utilizando o len() para saber a quantidade de alunos
for aluno in range(len(lista_alunos)):
    print(lista_alunos[aluno], end=' ')
    if c == 3:
        print()

print()
print('-'*50)
print('Fim do programa!')
print('-'*50)