# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Operadores Lógicos
# A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para auxiliar usuários na identificação desses anos de forma rápida e precisa. Eles precisam de um programa que permita aos usuários inserir um ano e, em seguida, determine se esse ano é bissexto ou não, de acordo com as regras estabelecidas pelo calendário gregoriano. Além disso, é necessário realizar a validação de entrada de dados para garantir que o ano inserido pelo usuário seja um valor válido, ou seja, um número inteiro positivo.


import os

os.system('cls')

print('-'*50)
print('LeapYearCheck: Calculando o ano bissexto!')
print('-'*50)

ano = int(input('Insira um ano: '))
resposta = ''

if ( ano % 4 == 0) and (ano % 100 != 0 ) or ( ano % 400 == 0):
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')

print('-'*50)
print(resposta)
print('-'*50)