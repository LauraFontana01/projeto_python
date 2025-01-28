# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025

import os


os.system('cls')

academia = {}

for i in range(1,2):
    equipamento = input('Insira o equipamento: ').lower()
    tipo = input('Tipo de equipamento: ')
    quantidade = int(input('Quantidade de equipamento: '))
    estado = input('Estado do equipamento: ').lower()

    academia[equipamento] = {'equipamento' : equipamento, 'tipo' : tipo,
                'quantidade' : quantidade, 'estado' : estado}
    

cardio = 0
for keys, values in academia.items():
    if values['tipo'] =='cardio':
        cardio += 1

reparo = 0 
for keys, values in academia.items():
    if values['estado'] == 'necessitando reparos':
        reparo += 1

while True:
    pergun = input('Deseja alterar alguma coisa? S/N: ').upper()
    if pergun == 'S':

        item_alterar = input('Qual item irá alterar? ')

        if item_alterar in academia:
            subitem_alterar = input('Qual valor irá alterar: ')

            if subitem_alterar in academia[item_alterar]:
                atualizar = input('Digite a alteração: ')

                if subitem_alterar == 'quantidade':
                    atualizar = int(atualizar)
                
                academia[item_alterar][subitem_alterar] = atualizar
        
        else:
            print('Não encontrado')
    
    elif pergun == 'N':
        print('Encerrando o programa..')
        print('=' * 70)
        print('Lista de equipamentos', equipamento)
        print('=' * 70)
        print('Lista de equipamentos de cardio: ',cardio )
        print('=' * 70)
        print('Lista de equipamentos necessitando reparo: ', reparo)
        print('=' * 70)
        break