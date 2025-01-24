# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Crie um programa para gerenciar o estoque de uma loja. Ele deve permitir:
# Cadastrar produtos com nome, quantidade em estoque e preço.
# Alterar a quantidade ou excluir um produto.
# Exibir os produtos cadastrados, organizados por nome.
# Gerar um relatório com o valor total do estoque (quantidade x preço).

import os 

os.system('cls')

produtos_dict = {}

for l in range(1,2):
    nome = input('Insira o nome do produto: ').lower()
    quantidade = int(input('Insira a quantidade: '))
    preco = float(input('Preço do produto: '))

    produtos_dict[nome] = {'nome' : nome ,'quantidade' : quantidade,
                    'preço' : preco}


while True:
    print('Menu de opções.')
    print('1. Alterar algo.')
    print('2. Deletar algo.')
    print('3. Sair.')
    opcao = input('Escolha uma das opções: ')

    if opcao == '1':
        item_alterar = input('Digite o item: ').strip().lower()

        if item_alterar in produtos_dict:
            alterar = input('Digite oque deseja alterar: ').strip().lower()

            if alterar in produtos_dict[item_alterar]:
                alteracao = input('Digite a alteração: ').strip().lower()
            
            else:
              print('Esse item não existe.')

        else:
          print('Esse item não existe.')

          produtos_dict[item_alterar][alterar] = alteracao
    
    elif opcao == '2':
       deletar = input('Qual item vai apagar: ')
       if deletar in produtos_dict:
          del produtos_dict[deletar]
    
    elif opcao == '3':
       print('Saindo')
       break
    
    else:
       print('Digite alguma das opções.')

produtos_em_ordem = sorted(produtos_dict.items(), key= lambda x: x[1])

for keys, values in produtos_dict.items():
    print(f'{keys}: {values}')

valor_total = sum(item['quantidade'] * item['preço'] for item in produtos_dict.values())

print(f'O valor atual é R${valor_total:.2f}')