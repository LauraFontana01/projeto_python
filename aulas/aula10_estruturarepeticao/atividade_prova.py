import os 


os.system('cls')


# crie um menu com 3 escolhas para o usuario 1) soma 2) mutilicação 3) sair

while True:
    print('1) Soma')
    print('2) Multiplicação')
    print('3) Sair')

    opcao = int(input('Digite sua opção: '))
    
    if opcao == 1:
        soma = 4 + 4
        print(soma)
    elif opcao == 2:
        multiplicacao = 5 * 7
        print(multiplicacao)
    else:
        break


# Faça o inverso: peça ao usuário para dar os numeros