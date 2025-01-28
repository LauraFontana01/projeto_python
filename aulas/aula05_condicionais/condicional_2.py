# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 28/10/2024

import os

os.system('cls')

# Declarações
a = 10
b = 5
resposta = ''

print('-'*50)
print('Estudo de Condicional (Simples)')
print('='*50)

# Condicionais
if a > b:
    resposta = f'{a} é maior que {b}'
else:
    resposta = f'{a} não é maior que {b}'

    #Saída
    print('-'*50)
    print(resposta)

# Declarações
a = 5
b = 5

print('-'*70)
print('Estudo de Condicional (aninhada)')
print('='*50)

if a > b:
    resposta = f'{a} é maior que {b}'
elif a < b:
    resposta = f'{a} é menor que {b}'
else:
    resposta = f'Os valores são iguais: {a} = {b}'

# Saida
print('-'*70)
print(resposta)
print('-'*70)
print()