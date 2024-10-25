# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Elabore um programa que receba quatro notas de um aluno e calcule a média dessas notas.

import os

os.system('cls')

print('-'*70)
print('Laurylin School\n Calculadora da média dos alunos')
print('-'*70)

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4°ª nota: '))         

# Processamento
media = ( nota1 + nota2 + nota3 + nota4) / 4

# Saida de dados
print(f'A média das seguintes notas\n {nota1}, {nota2}, {nota3} e {nota4} será {media}')
print('')