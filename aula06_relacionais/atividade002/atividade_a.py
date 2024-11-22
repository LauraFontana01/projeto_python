# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/10/2024
# Operadores Lógicos
# A empresa "TechSolutions" contratou você para desenvolver um programa em Python que irá automatizar uma parte do seu sistema de processamento de dados. Eles precisam de um programa que solicite ao usuário a entrada de um número inteiro e, em seguida, verifique se esse número é par ou ímpar. Essa funcionalidade é essencial para o sistema deles, pois eles processam grandes conjuntos de dados e precisam classificar os números de forma eficiente para realizar cálculos específicos em cada tipo de número.

import os


os.system('cls')

print('-'*50)
print('Processamento de Números TechSolutions')
print('-'*50)

#Entrada
numero = int(input('Digite um número: '))
resposta = ''


#Condicional
if numero % 2 == 0:  # operador == relacional ou comparação
    resposta = f'O número {numero} é par'
else:
    resposta = f'O número {numero} é ímpar'

#Saida
print('='*50)
print(resposta)

print('Fim do programa!\n') #\n salta uma linha