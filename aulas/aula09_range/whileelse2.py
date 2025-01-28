import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle While Else Break')
print('-'*50)

print()

while (True):

    # lower() garante o tratamento para entrada de 's' ou 'S'
    nome = str(input('Digite um nome [s - Sair]: ')).lower()

    if (nome != 's'):
        print('Continue digitando...')
    else:
        print('-'*50)
        print('Você digitou "s" para sair!')

        # interrompe o laço
        break

print('-'*50)
print()