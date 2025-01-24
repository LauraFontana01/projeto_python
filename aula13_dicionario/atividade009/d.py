# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Escreva um programa para cadastrar 5 tipos de vinho com 
# as informações: nome, tipo (tinto, rosé, etc.), teor alcoólico e safra. 
# O programa deve: Exibir uma lista detalhada com os vinhos cadastrados.
# Permitir modificar os dados de qualquer vinho.
# Gerar um relatório com:
# Vinhos com teor alcoólico superior a 12%.
# Vinhos com safra posterior a 2015.
# Lista de vinhos ordenados alfabeticamente.

import os


os.system('cls')

dicionario_vinho = {}


for vinhos in range(1, 3):
    numero = input('Insira o número do vinho: ')
    tipo = input('Tipo do vinho: ')
    teor = float(input('Insira o teor alcoólico: '))
    safra = int(input('Insira a safra: '))

    dicionario_vinho[numero] = {'tipo' : tipo, 'teor' : teor, 'safra' : safra}

alcool_alto = 0
safra_nova = 0

for keys, values in dicionario_vinho.items():
    if values['teor'] >= 12:
        alcool_alto += 1

for keys, values in dicionario_vinho.items():
    if values['safra'] >= 2015:
        safra_nova += 1


print(dicionario_vinho)

while True:
    alteracao = input('Vai alterar algo? S/N')
    if alteracao == 's':
        item_alterado = input('Digite o número do vinho: ')
            
        if item_alterado in dicionario_vinho:
            subitem_alterado = input('Digite o que quer alterar: ').strip().lower()

            if subitem_alterado in dicionario_vinho[item_alterado]:
                atualizacao = input('Digite a alteração: ')

                if subitem_alterado == 'teor alcoolico':
                        atualizacao = float(atualizacao)
                if subitem_alterado == 'safra':
                        atualizacao = int(atualizacao)
                        
                dicionario_vinho[item_alterado][subitem_alterado] = atualizacao
                print(dicionario_vinho)


            else:
                print('Esse item não esta disponivel')

    elif alteracao == 'n':
        break

print('=' * 70)
print('Dicionário', dicionario_vinho)
print('=' * 70)
print('Vinhos com teor acima de 12:', alcool_alto)
print('=' * 70)
print('Vinhos da safra de 2015 pra cima:', safra_nova)
print('=' * 70) 