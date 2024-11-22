# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 04/11/2024
# Biblioteca Math

# Faça um programa que receba as informações de base e expoente. Calcule a potência.


import os
import math


os.system('cls')

print('-'*50)
print('Calculadora de Potência')
print('~'*50)

base = float(input('Valor da base:'))
expoente = float(input('Valor do expoente: '))

potencia = math.pow(base, expoente)

print(f'{base} elevado a {expoente} é igual a: {potencia}')
      





