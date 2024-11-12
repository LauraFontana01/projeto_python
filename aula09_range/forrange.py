import os


os.system('cls')

print('-' * 50)
print('Estrutura de Controle For Range')
print('='*50)

print()

for var_iteradora in range (1, 7):
    print(f'Valor: {var_iteradora}', end=" | ")
    # end= coloca os numeros em uma mesma linha

print()
print()

# Ou

inicio = 1
fim = 7
passo = 2

for var_iteradora in range(inicio, fim, passo):
    print(f'Valor: {var_iteradora}', end=" | ")

print()
print()