# ímpares e Pares

import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle com Input e If')
print('-'*50)

print()

soma = 0 

for var_iteradora in range(0, 4):
    numero = int(input(f'{var_iteradora + 1}º número: '))

    if(numero % 2 == 0):
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')

print('-'*50)
print()