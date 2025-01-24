# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data de ínicio: 16/01/2025  | Data de finalização: 17/01/2025
# Crie um programa para organizar filmes em um cinema. Ele deve:
# Cadastrar 5 filmes com título, gênero, duração e classificação indicativa.
# Permitir alterar informações, se necessário.
# Listar todos os filmes, organizados por título.
# Gerar um relatório com:
# Quantos filmes têm duração maior que 2 horas.
# Quantos filmes têm classificação indicativa "livre".

import os


os.system('cls')

print('-'*50)
print('Filmes em cartaz - Cinema GoodMovies')
print('º'*50)

filmes = {}
filmes_longos = 0 

for i in range(5):
    titulo = input('Insira o título do filme: ').lower()
    genero = input('Gênero do filme: ').lower()
    duracao = int(input('Duração do filme (em minutos): '))
    classificacao = (input('Classificação Indicativa do filme: ')).lower()
    print('-'*50)

    if duracao > 120:
        filmes_longos += 1

    filmes[titulo] = {'Título' : titulo, 'Gênero' : genero, 
            'Duração' : duracao, 'Classificação indicativa' : classificacao}

livre = 0
for keys, values in filmes.items():
    if values['Classificação indicativa'] == 'livre':
        livre += 1

while True:
    quest = input('Gostaria de alterar algo? (S/N): ').upper()

    if quest == 'S':
        item_alterado = input('Digite o título do filme: ').lower()

        if item_alterado in filmes:
            subitem_alterado = input('O que será alterado?: ').lower().strip()

            if subitem_alterado in filmes[item_alterado]:
                atualizar = input('Insira a alteração: ')

                if subitem_alterado == 'duracao':
                    atualizar = int(atualizar)
                
                if subitem_alterado == 'classificacao':
                    atualizar = int(atualizar)

                filmes[item_alterado][subitem_alterado] = atualizar
                
        else:
            print('Esse item não está disponível!')

    elif quest == 'N':
        print('Encerrando o sistema!')
        print('-'*50)
        print('Lista dos filmes', filmes)
        print('-'*50)
        print('Filmes com mais de 2 horas: ',filmes_longos )
        print('-'*50)
        print('Filmes com a classificação livre: ', livre)
        print('-'*50)
        ordem = sorted(filmes.values(), key= lambda x: (x['Título']))
        for titulo in ordem:
            print('Lista de filmes em ordem: ' ,titulo['Título'])
        break