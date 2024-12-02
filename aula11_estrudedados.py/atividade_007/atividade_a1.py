# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# A) Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). Após esta entrada de dados, faça o seguinte:
#• Mostre a quantidade de notas que foram lidas.
#• Exiba todas as notas na ordem em que foram informadas.
#• Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
#• Calcule e mostre a soma das notas.
#• Calcule e mostre a média das notas.

import os


os.system('cls')

# Entrada do titulo
print('-'*50)
print('Programa de Notas')
print('-'*50)

# Entrada
lista_notas = []

quantidade = 0
soma = 0

# Iteração das notas
print('Insira as notas. Digite "s" ou "0" para sair.')
print('.' * 70)
while True:
    nota = input('Digite uma nota: ').strip().lower()
    print('-' * 70)

    # Condição de quebra de laço
    if nota == 's' or nota == '0':
        break

    # Inserção de valores na lista
    lista_notas.append(float(nota))

    # Contagem de notas inseridas
    quantidade += 1
print()

# Lista inversa a partir da inserção
lista_inversa = lista_notas[::-1]

# Soma dos elementos da lista
for i in range(len(lista_notas)):
    soma += lista_notas[i]

# Cálculo da média das notas
media = soma / quantidade

# Saída
print('=' * 70)
print(f'Quantidade de notas inseridas na lista: {quantidade}')
print('-' * 70)
print(f'Lista de notas inseridas: {lista_notas}')
print('-' * 70)

# Iteração da lista das notas para saída de elementos
print(f'Lista de notas inversa conforme inserção:')
for i in range(len(lista_inversa)):
    print(lista_inversa[i])
print('-' * 70)

# Saída
print(f'A soma das notas é: {soma:.1f}')
print('-' * 70)
print(f'A média das notas é: {media:.1f}')
print('=' * 70)
print()