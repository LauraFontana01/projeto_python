# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 05/11/2024
# String em Python
# Faça um programa que receba um número inteiro e mostre na tela a quantidade de unidades, a quantidade de dezenas, a quantidade de centenas e a quantidade de milhares
# Não utiliza as regras de string e sim, continha matematica top

import os


os.system('cls')

print('.'*50)
print('Quantidade de unidades, dezenas, centenas e milhares!')
print('~'*50)

numero = int(input('Digite um número: '))


if numero > 9999:
    print('Número Inválido!')
    exit()
else:
    milhar = numero // 1000
    centena = (numero % 1000) // 100
    dezena = (numero % 100) // 10
    unidade = (numero % 10) // 1

print(f'Milhar: {milhar}; centena: {centena}; dezena: {dezena} e unidade {unidade}')