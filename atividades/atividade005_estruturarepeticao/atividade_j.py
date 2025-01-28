# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 18/11/2024
# Estrutura de Repetição

# Crie um programa que realiza a contagem de 1 até 100, 
# usando apenas de números ímpares, 
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo,
# assim como a soma dos mesmos.

import os


os.system('cls')

contador_quantidade = 0
contador_soma = 0

for numero in range(1, 101):
    if numero % 2 != 0:
        contador_quantidade += 1
        contador_soma += numero
print(f'Quantidade de números ímpares: {contador_quantidade}')
print(f'Soma dos números: {contador_soma}')