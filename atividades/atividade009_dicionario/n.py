# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# 

import os


os.system('cls')

produtos = {}

for i in range(1,2):
    nome = input('Insira o nome do produto: ').lower()
    preco = float(input('Preço do produto: '))
    categoria = input('Categoria do produto: ')
    desconto = float(input('Digite o desconto: '))

    produtos[nome] = {'nome' : nome, 'preço' : preco, 'categoria' : categoria,
                    'desconto' : desconto}



while True:
    print('Responda com S ou N')
    mudar_preco = input('Deseja alterar algum preço: ').lower()
    

    if mudar_preco == 's':
        prod_preco = input('Digite o nome do produto: ')

        if prod_preco in produtos:
            preco_novo = int(input('Digite o novo preço: '))
            calculo = preco_novo - (preco_novo * desconto / 100)
            produtos[prod_preco]['preço'] = calculo
        else:
            print('Produto não existe.')

    elif mudar_preco == 'n':
        break

barato = 0
eletro = 0

for keys, values in produtos.items():
    if values['preço'] < 50:
        barato += 1

    if values['categoria'] == 'eletronico':
        eletro += 1


for keys, values in produtos.items():
    print(f'{keys}: {values}')
    
print(f'{barato} itens com o preço menor que 50 pila')
print(f'{eletro} itens eletronicos.')