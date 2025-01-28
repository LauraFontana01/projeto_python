# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Estudos da biblioteca Math

import math
import os


os.system('cls')

print('-'*50)
print('Estudos da Biblioteca Matemática MATH')
print('~'*50)

# Entrada de dados
numero_decimal = float(input('Entre com um número decimal: '))

# Processamento
arredondar_para_cima = math.ceil(numero_decimal)
arredondar_para_baixo = math.floor(numero_decimal)

# Saida
print('~'*50)
print(f'O número {numero_decimal} arredondado para cima é: {arredondar_para_cima}')
print(f'O número {numero_decimal} arredondado para baixo é: {arredondar_para_baixo}')
print('-'*50)