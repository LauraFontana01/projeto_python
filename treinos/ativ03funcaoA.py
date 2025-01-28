# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Biblioteca Math
# Faça um programa que receba um valor e mostre sua raiz quadrada. Para raízes que não são exatas, arredonde para cima ou para baixo. 
# Faça a validação para números negativos, avisando ao usuário que o resultado será um número complexo.

import os 

import math


os.system('cls')

print('-'*50)
print('Calculadora de Raiz Quadrada')
print('-'*50)

numero = float(input('Digite um número: '))



if numero < 0:
    print('O resultado será um número complexo!')
else:
    raizquadrada = math.sqrt (numero)
    arredondar_acima = math.ceil(raizquadrada)
    print(f'A raiz quadrada de {numero} é: {arredondar_acima}')


print(f'-'*50)