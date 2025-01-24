# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/01/2025
# Crie uma função que receba a altura e  peso de uma pessoa. 
# Depois retorne o seu IMC.

import os


os.system('cls')

# Título
print('-'*50)
print('Calculadora do IMC :)')
print('-'*50)

# Definição da função chamada de "calculando" recebe parâmetro "altura, peso"
def calculando(altura, peso):
    # Cálculo do IMC
    imc = peso / (altura ** 2)
    return imc

# Entrada do usuário
altura = float(input('Insira a sua altura: '))
print('-'*50)
peso = float(input('Insira o seu peso: '))
print('-'*50)

# Invocação da função
imc2 = calculando(altura, peso)

# Saída
print(f'Cálculo do IMC: {imc2:.2f}')
print('-'*50)