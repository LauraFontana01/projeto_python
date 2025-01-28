# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Operadores Lógicos
# Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo. Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si. A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.
# programa precisa receber as medidas dos três segmentos e compará-las entre si. A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

# atividade 002 -  equação de segundo grau

import os

os.system('cls')

print('-'*50)
print('Três segmentos podem formar um triângulo?')
resposta = ''

a = float(input('1ª Medida: '))
b = float(input('2ª Medida: '))
c = float(input('3ª Medida: '))
print('')

if (a + b > c) and ( b + c > a) and ( a + c > b):
    print('Esses segmentos formam um triângulo!')
else:
    print(' Esses segmentos não formam um triângulo!')

print('-'*50)
print(resposta)
print('-'*50)


