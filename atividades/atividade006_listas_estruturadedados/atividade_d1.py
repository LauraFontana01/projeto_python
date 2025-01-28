# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# D) Faça um programa que preencha uma lista com as notas de 4 alunos, depois imprima a média.

import os


os.system('cls')

print('-'*50)
print('Cálculo de médias')
print('-'*50)


# Lista para armazenar notas
lista_notas = []

# Flag
soma_de_notas = 0

# Iteração 4 notas
for notas in range(1, 5):
    aluno = float(input(f'Digite a nota do aluno {notas}: '))
    lista_notas.append(f'{aluno:.2f}')

    soma_de_notas += aluno

    media = soma_de_notas / 4


print('-'*50)
print(f'A média dos alunos é: {media}')
