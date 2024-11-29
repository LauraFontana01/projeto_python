# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/11/2024

import os


os.system('cls')

# Solicitar ao usuário a quantidade de elementos na tupla
numero_elementos = int(input('Quantos elementos na tupla? '))

# Inicializar uma lista vazia para armazenar os elementos
elementos = []

# Estrutura de repetição para obter os elementos do usuário
for i in range(numero_elementos):
    while True:
        valor = input(f'Digite o valor {i + 1}: ')
        if valor.isdigit(): #Verificar se a entrada é um número
            elementos.append(int(valor))
            break
        else:
            print('Entrada Inválida! Digite um número.')

# Converter a lista para uma tupla
tupla = tuple(elementos)

print('-'*50)
# E xibir a tupla criada
print(f'Tupla criada: {tupla}')
print('-'*50)

# Estrutura de repetição para permitir múltiplas operações
# até que o usuário deseje sair
while True:
    # Condicional para verificar a presença de
    # um número específico
    valor = int(input('Verificar se o número na Tupla: '))

    if valor in tupla:
        print(f'O número {valor} está na tupla.')
        # Contar quantas vezes o número aparece

        contagem = tupla.count(valor)
        print(f'O número {valor} aparece {contagem} vez(es).')
        # Encontrar o índice da primeira ocorrência

        indice = tupla.index(valor)
        print(f'A 1ª ocorrência de {valor} está no índice {indice}.')

    else:
        print(f'O número {valor} não está na tupla.')

    # Perguntar ao usuário se deseja realizar
    # outro operação ou sair
    continuar = input('Deseja Continuar? (s/n): ').lower()
    if continuar != 's':
        print('Encerrando o programa. Até mais!')
        break
print('-'*50)
print('Fim do programa!')
print()