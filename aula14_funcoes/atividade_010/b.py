# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/01/2025
# Crie uma função que cadastre o nome de um aluno(a), 
# a matrícula e a data de nascimento. 
# Depois imprima os resultados cadastrados utilizando 
# uma estrutura de repetição for.

import os


os.system('cls')

# Definição da função
def aluno(nome,matricula,data):
    return nome, matricula, data

# Recebendo os dados do aluno
nome = input('Insira o nome do aluno: ')
print('-'*50)
matricula = int(input('Insira o número de matrícula: '))
print('-'*50)
data = input('Insira a data de nascimento: ')
print('-'*50)
# Chamando a função para cadastrar o aluno
cadastro = aluno(nome, matricula, data)

# Saída com FOR
for i in cadastro:
    print(i)
