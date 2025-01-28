# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 28/01/2025

import os


from modulos.modulo_somar import somar
from modulos.modulo_multi import multiplicar as multi
from modulos.modulo_dividir import dividir


while True:
    os.system('cls')

    a = input('Entre com o valor de A: ')
    b = input('Entre com o valor de B: ')

    if not a.replace('.', '', 1).isdigit() or not b.replace('.', '', 1).isdigit():
        print('Por favor, entre com um número válido.')
        continue

    a = float(a)
    b = float(b)

    resultado_soma = somar(a, b)
    resultado_produto = multi(a, b)
    resultado_divisao, erro = dividir(a, b)

    print('-'*50)
    print('Cálculos Matemáticos')
    print('-'*50)
    print(f'Cálculo da soma: {resultado_soma}')
    print(f'Cálculo do produto: {resultado_produto}')
    print(f'Cálculo da divisão: {resultado_divisao}, {erro}')
    print('-'*50)

    sair = input('Deseja sair do programa? (s/n): ').strip().lower()
    if sair == 's':
        print('Saindo do programa')
        break