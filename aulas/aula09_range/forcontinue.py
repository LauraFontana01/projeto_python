import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle: Continue')
print('-'*50)

print()

for c in range(1, 11):
    if c == 5:
        # 5 está fora do loop, se retirar a linha de abaixo,
        #ele não aparecera na saída, deixei para verificação!
        print(f'O número {c} está fora do loop!')
        continue     # Salta e o ciclo continua

    print(f' o número é {c}')

print('-'*50)
print()