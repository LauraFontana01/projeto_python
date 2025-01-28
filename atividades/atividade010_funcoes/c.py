# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/01/2025
# Crie uma função que verifica se um aluno(a) está cadastrado 
# ou não em um dicionário. Se estiver cadastrado, 
# imprima o nome desse aluno e o resto dos seus dados. 
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')

print('-'*50)
print('Cadastro de Alunos - High School Musical')
print('-'*50)

alunos_dict = {}

alunos_lista = []

# Definição da função
def aluno(nome,matricula,data):
    return {'Nome': nome, 'Matrícula': matricula, 'Data de nascimento': data}

# Looping
for n in range(2):
    # Recebendo os dados do aluno
    nome = input('Insira o nome do aluno: ').capitalize().strip()
    print('-'*50)
    matricula = int(input('Insira o número de matrícula: '))
    print('-'*50)
    data = input('Insira a data de nascimento: ')
    print('~'*50)

# Colocando dentro da lista
    aluno_cadastro = aluno(nome,matricula,data)
    alunos_lista.append(aluno_cadastro)

print(f'Lista de alunos: {alunos_lista}')
print('-'*50)

pergunta = input('Qual aluno irá verificar: ').capitalize().strip()
print('-'*50)
# Verificando se o aluno está na lista
for n in alunos_lista:
    if n['Nome'].capitalize() == pergunta.capitalize():
        print('Nome: ',n['Nome'])
        print('Matrícula: ',n['Matrícula'])
        print('Data de nascimento: ',n['Data de nascimento'])
        break
else:
    print('Aluno não cadastrado.')