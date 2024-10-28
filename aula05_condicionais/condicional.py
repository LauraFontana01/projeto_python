# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 28/10/2024

import os 

os.system('cls')

print('-'*50)
print('Estudo de Condicional :  Parte 1')
print('='*50)

#Entrada
numero = float(input('Digite um número: '))
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