# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/11/2024
# Atividade de Estrutura de Dados

# F) Faça um programa que leia 5 nomes, 
# depois imprima estes nomes com seus respectivos índices. 
# enumerate - retorna partes de índice e valor durante a iteração

# usamos append para inserir os nomes na lista

print('-'*50)
print('Nomes e seus índices')
print('-'*50)

# Lista
lista_nomes = []

# Entrada de dados
for i in range(1, 6):
    nomes = input(f'Digite o {i}º nome: ')
    
    # Inserção dos nomes na lista
    lista_nomes.append(nomes)


# Enumeração do Índice
print('-'*50)
for indice, nome in enumerate(lista_nomes):
    print(f'Índice: {indice} | Nome: {nome}')

# Saída 
print(f'Nomes: {lista_nomes}')

