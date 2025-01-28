# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Faça um programa para cadastrar alunos de uma escola. Ele deve:
# Registrar 5 alunos com nome, data de nascimento e número de matrícula.
# Permitir alterar os dados dos alunos cadastrados.
# Exibir a lista de alunos com suas informações.
# Gerar um relatório que mostre:
# Quantos alunos nasceram após o ano 2000.
# Quantos têm números de matrícula ímpares.
# Mostrar os dados de um aluno específico ao buscar pelo número de matrícula.

import os

os.system('cls')


dicionario_alunos = {}

for alunos in range(1, 3):
    nome = input('Nome do aluno: ')
    datanasci = int(input('Data de nascimento: '))
    matricula = int(input('Número de matrícula: '))

    dicionario_alunos[matricula] = {'matricula': matricula, 'nome' : nome,
                    'nascimento' : datanasci}

doismil = 0
impar_matri = 0

for keys, values in dicionario_alunos.items():
    if datanasci >= 2000:
        doismil += 1

if matricula % 2 != 0:
    impar_matri += 1

while True:
    print('OPÇÕES')
    print('1 - Alterar informações')
    print('2 - Buscar aluno')
    print('3 - Sair')
    resposta = input('Escolha alguma das opções: ')

    if resposta == '1':
        item_alterado = input('Digite o nome do aluno: ')

        if item_alterado in dicionario_alunos:
            subitem_alterar = input('Digite o que quer alterar: ').strip().lower()

            if subitem_alterar in dicionario_alunos[item_alterado]:
                atualizar = input('Digite a alteração: ')

                if subitem_alterar == 'nascimento':
                    atualizar = int(atualizar)
                if subitem_alterar == 'matricula':
                    atualizar = int(atualizar)
                
                dicionario_alunos[item_alterado][subitem_alterar] = atualizar

    elif resposta == '2':
        aluno_sele = int(input('Insira o número de matricula: '))
        if aluno_sele in dicionario_alunos:
            print(dicionario_alunos[aluno_sele])
        
        else:
            print('Este aluno não existe')
    
    elif resposta == '3':
        print('Encerrando o programa..')
        print('=' * 70)
        print('Lista de alunos', dicionario_alunos)
        print('=' * 70)
        print('Alunos que nasceram depois de 2000: ',doismil)
        print('=' * 70)
        print('Alunos com matricula impar: ', impar_matri)
        print('=' * 70)
        break