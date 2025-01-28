# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Operadores Lógicos
# A empresa "SalaryBoost" está implementando um sistema automatizado para calcular os aumentos salariais de seus funcionários com base em critérios específicos. Eles precisam de um programa que receba como entrada o salário atual de um funcionário e, em seguida, calcule o novo salário com base em determinadas condições. Essas condições incluem um aumento de 5% caso o salário atual seja superior a R$1500,00, e um aumento de 10% caso o salário atual seja inferior a R$1000,00. Além disso, o programa deve garantir que o salário informado não seja igual a zero ou negativo, pois isso não seria válido.
# programa que receba como entrada o salário atual de um funcionário e, em seguida, calcule o novo salário com base em determinadas condições

import os

os.system('cls')

print('-'*50)
print('Calculadora do Aumento Salarial')
print('-'*50)

# Entrada sem processamento
salario_atual = float(input('Digite o salário atual: '))
resposta = ''

# Processamento
if (salario_atual > 1500):
    reajuste_1 = salario_atual * 0.05
    print( f'O salário reajustado será R${salario_atual + reajuste_1:.2f}!')
elif (salario_atual <= 1500) and (salario_atual >= 1000):
    print( f'O salário não terá mudanças!')
else:
    reajuste_2 = salario_atual * 0.1
    print( f'O salário reajustado será R${salario_atual + reajuste_2:.2f}!')

print(resposta)
print('-'*50)