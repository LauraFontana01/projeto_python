# A) Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). Após esta entrada de dados, faça o seguinte:
#• Mostre a quantidade de notas que foram lidas.
#• Exiba todas as notas na ordem em que foram informadas.
#• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
#• Calcule e mostre a soma das notas.
#• Calcule e mostre a média das notas.

import os


os.system('cls')

print('-'*50)
print('Leitor de Notas')
print('-'*50)

# Flag
notas = 0

# Armazenamento das notas
lista = []

# Looping
while True: 
    nota = input('Digite a nota: ')

    if nota == 's' or nota == '0':
        break

    lista.append(nota)

    # Contagem da quantidade de notas inseridas
    notas += 1

print('-'*50)
print(f'Notas lidas: {notas}')
print('-'*50)
print(f'Ordem das Notas: {lista}')
