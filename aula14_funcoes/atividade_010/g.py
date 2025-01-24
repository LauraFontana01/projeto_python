# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 22/01/2025
# Crie um programa que peça ao usuário 2 números maiores que 0 e menores que 11.
# Depois mostre um menu com as seguintes operações:
# 1. Soma: 2. Subtração : 3. Produto : 4. Divisão : 5. Divisão inteira : 6. Resto da divisão.
# O usuário deverá escolher um número maior ou  igual a 1 e menor ou igual a 6.
#  Em seguida, você criará funções que retornem os resultados das operações, 
# imprimindo os resultados na tela.

import os

# Definir função limpar terminal "def function()"
def clear_terminal():
    os.system('cls')

# Definir função números "def function(a, b = int, c = int)"
def get_numbers(prompt, min_value = 1, max_value = 10):
    print('=' * 80)
    # Criar loop iteração usuário "while bool:"
    while True:

        # Iterar usuário número "a = input(arg_1)"
        num_1 = input(prompt)

        # Condicionar número inteiro "if a.isdigit():"
        if num_1.isdigit():

            # Fazer casting inteiro "a = int(a)"
            num_1 = int(num_1)

            # Condicionar existência número "if arg_2 <= a <= arg_3"
            if min_value <= num_1 <= max_value:
                return num_1
        
            # Fechar condição "else:"
            else:
                print('-' * 80)
                print('Número inválido. Tente novamente.')
                print('-' * 80)

# Definir função operação "def function(a, b, c):"
def perform_operation(numbers, operation, numb_operator):

    # Separar elementos "a, b = arg_1"
    op_1, op_2 = numbers

    # Condicionar operação "if a == int:"
    if operation == 1:

        # Somar "a = elem + arg_2"
        result_1 = op_1 + numb_operator
        result_2 = op_2 + numb_operator

        # Retornar resultado "return a, b"
        return result_1, result_2

    # Subtrair "a = elem + arg_2"
    elif operation == 2:
        result_1 = op_1 - numb_operator
        result_2 = op_2 - numb_operator

        # Retornar resultado "return a, b"
        return result_1, result_2

    # Multiplicar "a = elem * arg_2"
    elif operation == 3:
        result_1 = op_1 * numb_operator
        result_2 = op_2 * numb_operator

        # Retornar resultado "return a, b"
        return result_1, result_2

    # Dividir "a = elem / arg_2"
    elif operation == 4: 
        result_1 = op_1 / numb_operator
        result_2 = op_2 / numb_operator

        # Retornar resultado "return a, b"
        return result_1, result_2
    
    # Divisão inteira "a = elem // arg_2"
    elif operation == 5:
        result_1 = op_1 // numb_operator
        result_2 = op_2 // numb_operator

        # Retornar resultado "return a, b"
        return result_1, result_2

    # Resto da divisão "a = elem % arg_2"
    elif operation == 6:
        result_1 = op_1 % numb_operator
        result_2 = op_2 % numb_operator

        # Retornar resultado "return a, b"
        return result_1, result_2

# Definir função menu "def function()"
def print_menu():
    print('=' * 80)
    print('Menú de opções')
    print('=' * 80)
    print('1. Somar (+).')
    print('2. Subtrair (-).')
    print('3. Multiplicar (*).')
    print('4. Dividir (/).')
    print('5. Calcular divisão inteira (//).')
    print('6. Calcular resto de divisão (%).')
    print('7. Sair.')
    print('=' * 80)


# Programa Principal:
print('=' * 80)
print('FUNÇÃO - OPERAÇÕES')
print('=' * 80)
print()

# Receber números em lista "list = [function(f'str') for i in range(int)]"
numbers = [
    get_numbers(f'Digite o {i + 1}º número (1-10): ') for i in range(2)
]
print('=' * 80)
print()

# Criar loop menu "while bool:"
while True:

    # Chamar função "a = function()"
    menu = print_menu()
    print()

    # Chamar função números "a = function(value_1, value_2, value_3)"
    option = get_numbers('Escolha uma opção (1-7): ', 1, 7)
    print('=' * 80)
    print()

    if option == 7:
        print('=' * 80)
        print('Sistema encerrado.')
        print('=' * 80)
        print()
        break

    # Chamar função números "a = function(value_1, value_2, value_3)" 
    numb_operator = get_numbers('Digite um número operador (1-6): ', 1, 6)
    print('=' * 80)
    print()

    # Chamar função operação "a, b = function(value_1, value_2, value_3)"
    result_1, result_2 = perform_operation(numbers, option, numb_operator)

    print('=' * 80)
    print(f'Resultado 1: {result_1}')
    print(f'Resultado 2: {result_2}')
    print('=' * 80)
    print()

    print('=' * 80)
    input('Pressione Enter para continuar.\n')

    # Chamar função limpeza terminal "a = function()"
    cls_terminal = clear_terminal()

