# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 04/11/2024
# Biblioteca Math

#Faça um programa que receba 2 valores, faça a divisão entre eles. Se a divisão não for inteira, o programa deverá arredondar o resultado para cima e para baixo. Faça a validação para divisão por 0.

import os
import math


os.system('cls')

print('-'*50)
print('Divisão Arredondada De Valores')
print('-'*50)

numerox = float(input('Digite um número: '))
numeroy = float(input('Digite outro número: '))

resultado = numerox / numeroy

if numeroy == 0:
    print('É impossivel divir algum número por 0!')
elif (resultado) == float:
    arredondar_acima = math.ceil(resultado)
else:
    print(f'O resultado da divisão é {resultado}')

print('~'*50)