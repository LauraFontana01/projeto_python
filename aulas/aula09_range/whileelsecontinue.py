import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle While, Else, Continue')
print('-'*50)

print()

contador = 0 #Flag

while (contador <= 10):

    # Soma o contador
    contador += 1 # é o mesmo que contador = Contador + 1

    if (contador % 2 == 0): # pulando os pares
        continue
    print(f'Contador = {contador}')
else:
    print(f'Bloco do while...else: contador em {contador}!')

print('-'*50)
print('Fim do programa!')
print()