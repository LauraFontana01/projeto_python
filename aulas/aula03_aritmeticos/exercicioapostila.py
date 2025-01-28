# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 24/10/2024
# 

import os

import datetime

os.system('cls')

print('-'*70) # firulinha visual
print('WELCOME TO CODELAND!!!')
print('-'*70) # firulinha visual

# Entrada com Casting
nome = str(input('Seu nome:'))
nascimento = int(input('Ano de nascimento: '))
linguagem = str(input('Tipo de linguagem de programação que você usa: '))
cidade = str(input('Cidade que reside: '))
numero = int(input('Número de celular: '))

# Processamento: Pegando o ano corrente
ano_atual = datetime.datetime.now().year
idade = int(ano_atual) - nascimento

# Saida
print('-'*70)
print('SAÍDA DE DADOS')
print('='*70)
print('Nome................: ', nome)
print('Ano de nascimento.........: ', nascimento)
print('Linguagem.........: ', linguagem)
print('Cidade..........: ', cidade)
print('Numero........: ', numero)

# Saida interpolada
print(f'{nome}, você tem {idade} anos! Você usa {linguagem} como linguagem de programação! Sei que você gosta de estudar e sugiro que continue assim! Beijos de luz!')
print(f'Linguagem..............: {linguagem}')
print(f'Cidade........: {cidade}')
print(f'Numero........: {numero}')
print('-'*70)
print('')