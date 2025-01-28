# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 30/10/2024
# Operadores Lógicos
#  A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de preços de passagens de ônibus com base na distância da viagem. Eles precisam de um programa que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com as políticas da empresa. Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.
# programa que solicite ao usuário a distância a desejada e, em seguida, calcule o preço da passagem de acordo com as políticas da empresa. Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por km rodado, enquanto viagens acima dessa distância passam a custar R$0,40 por km rodado.

import os

os.system('cls')

# Entrada
print('-'*50)
print('TravelCalc: Calculando suas passagens!')
print('-'*50)

# Processamento
distancia = float(input('Insira a distância a ser percorrida em KM: '))
resposta = ''

if (distancia <= 200):
    tarifa_1 = distancia * 0.70
    print(f'O valor da sua passagem será R${tarifa_1:.2f}')
else:
    tarifa_2 = distancia * 0.40
    print(f'O valor da sua passagem será R${tarifa_2:.2f}')

print('-'*50)
print(resposta)






