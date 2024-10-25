# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 25/10/2024
# Crie um programa que converta uma medida em metros para centímetros e milímetros.

import os

os.system('cls')

print('-'*70)
print('Eu consigo calcular uma medida em metros para centrimetros e milimetros! Tenta ai!')
print('-'*70)

# Entrada
m = float(input('Digite uma metragem: '))

# Processamento
cm = m * 100
mm = m * 1000

# Saida
print('-'*70)
print(f'A medida fornecida convertida para centimetros resulta em: {cm:.2f} cm')
print(f'A medida fornecida convertida para milimetros resulta em: {mm:.2f} mm')
print('-'*70)