import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle: Break')
print('-'*50)

print()

for c in range(0, 10):

    print(f'Valor: {c}')

    # Condição para terminar a contagem
    if (c == 5):
        print(f'Contagem Interrompida no {c}')
        break

print('-'*50)
print('Fim do programa!')
print()