import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle, Validação e Casting')
print('-'*50)

soma = 0

for c in range(0, 5):

    numero = input('Digite um número [0-5]: ')

    # Validação
    if (not (numero.isnumeric())):
        print(f'"{numero}" Entrada Inválida!')
        print()
    else:
        # Casting da variável, ou seja, vai virar um inteiro
        numero = int(numero)

        # Validando o intervalo pedido
        if (numero >= 0 and numero <= 5):
            print(f'O número {numero} está dentro do intervalo [0-5]!')
            print()

print('-'*50)
print()