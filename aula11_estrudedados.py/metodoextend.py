# ele cata um negocio e insere 
# ele pega uma lista e outra lista e une as duas, sem misturar, junção

import os


os.system('cls')

# Inicializa a lista vazia
lista_numeros = [100, 200]

# Solicita ao usuário para inserir números separados por espaço
entrada = input('Digite números separados por espaço: ')

# Divide a string de entrada em uma lista de string
numeros = entrada.split()

# Cria uma lista para armaenar os números pares
pares = []

# Itera sobre os números inseridos
for numero in numeros:
    # Converte a string para inteiro
    numero_aux = int(numero)
    # Verifica se o número é par
    if numero_aux % 2 == 0:
        # Adiciona o número par à lista de pares
        pares.append(numero_aux)
print('-'*50)
print(f'Lista gerada: {pares}')
print('-'*50)

# Usa extend() para adicionar todos os números pares à lista principal
lista_numeros.extend(pares)

# Exibe a lista resultante 
print(f'Números pares adicionados à lista: {lista_numeros}')