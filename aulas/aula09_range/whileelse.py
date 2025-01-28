import os


os.system('cls')

print('-'*50)
print('Estrutura de Controle While Else')
print('-'*50)
print()

print()

contador = 1

while contador < 7:
    print("Contador é:", contador)
    contador += 1

    # Se eu tirar essa condicional o else será excluido
    if contador == 4:
        print(f"Contador chegou em {contador}. Break no While!")
        break
else:
    print("While finalizado!")

print()