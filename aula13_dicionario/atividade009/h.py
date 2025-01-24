# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
#  Faça um programa para gerenciar livros de uma biblioteca. Ele deve:
# Cadastrar 5 livros com título, autor, ano de publicação e número de páginas.
# Permitir alterações nos dados dos livros cadastrados.
# Exibir todos os livros organizados por título.
# Gerar um relatório que mostre:
# Quantos livros têm mais de 300 páginas.
# Quantos são do autor "J.K. Rowling".

import os

os.system('cls')

livros_dic = {}

for l in range(1,4):
    titulo = input('Insira o titulo do livro: ').lower()
    print('=' * 70)
    autor = input('Insira o nome do autor: ').lower()
    print('=' * 70)
    ano_publi = int(input('Insira o ano de publicação: '))
    print('=' * 70)
    num_pag = int(input('Insira o número de páginas: '))
    print('=' * 70)

    livros_dic[titulo] = {'titulo' : titulo ,'autor' : autor, 'ano': ano_publi,
                        'páginas': num_pag}
    print(livros_dic)

muitas_pag = 0
mesmo_autor = 0


for keys, values in livros_dic.items():
    if values['páginas'] >= 300:
        muitas_pag += 1

for keys, values in livros_dic.items():
    if values['autor'] == 'j.k rolling':
        mesmo_autor += 1

while True:
    pergun = input('Deseja alterar algo? S/N: ').upper()

    if pergun == 'S':
        item_alterado = input('Qual o titulo: ')

        if item_alterado in livros_dic:
            subitem_alterar = input('Digite oque quer alterar: ').lower().strip()

            if subitem_alterar in livros_dic[item_alterado]:
                atualizar = input('Digite a alteração: ')

                if atualizar == 'ano':
                    atualizar = int(atualizar)
                
                if atualizar == 'paginas':
                    atualizar = int(atualizar)
                
                livros_dic[item_alterado][subitem_alterar] = atualizar

        
        else:
            print('Esse livro não está cadastrado')
    
    else:
        print('Encerrando o programa..')
        print('=' * 70)
        print('Lista livros', livros_dic)
        print('=' * 70)
        print('Livros com mais de 300 páginas', muitas_pag)
        print('=' * 70)
        print('Livros com o autor J.K Rolling', mesmo_autor)
        print('=' * 70)
        ordem = sorted(livros_dic.values(), key= lambda x: (x['titulo']))
        for titulo in ordem:
            print('Lista dos livros em ordem', titulo['titulo'])
        break