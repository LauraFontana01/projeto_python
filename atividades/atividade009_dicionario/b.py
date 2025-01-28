# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# Desenvolva um programa onde o usuário cria um dicionário 
# com 5 chaves (nomes de cores) e seus valores (descrições ou códigos).
# Após o cadastro, exiba o dicionário ordenado pelas cores
# e mostre a quantidade de cores por cada letra inicial.

import os


os.system('cls')

# Título
print('-'*50)
print('Relatório ordenado de dicionário de cores')
print('-'*50)

# Dicionario "dict = {}"
color_dict = {}

# Iterar 5 cores "for i in range(value)"
for i in range(5):
    color = input(f'Digite a {i + 1}ª cor: ').strip().capitalize()
    print('-'*50)
    code = input(f'Descrição ou código da {i + 1}ª cor: ').strip().capitalize()
    print('-'*50)

    # Adicionar par cor-código ao dict "dict[key] = value"
    color_dict[color] = code

# Looping Menu "while true"
while True:

    # Limpar terminal 
    os.system('cls')

     # Ordenar dict pela chave "dict_2 = sorted(dict.items())"
    dict_ordem = sorted(color_dict.items())
    
    # Exibir dict inicial ordenado "for key, value in dict.items()"
    print('=' * 80)
    print('Dicionário Atual: ')
    print('-' * 80)
    for key, value in dict_ordem:
        print(f'{key}: {value}')
    print('=' * 80)
    print()
    
    # Menu
    print('=' * 80)
    print('Menu de opções:')
    print('-' * 80)
    print('1. Adicionar par "cor - descrição."')
    print('-' * 80)
    print('2. Modificar descrição de uma cor.')
    print('-' * 80)
    print('3. Gerar relatório ordenado de quantidade "cores / letra".')
    print('-' * 80)
    print('4. Sair.')
    print('-' * 80)
    option = input('Digite uma opção (1-4): ')
    print('=' * 80)
    print()
    
    # Adicionar par "cor - descrição"
    if option == '1':
        print('=' * 80)
        color = input('Digite a cor: ').strip().capitalize()
        print('-' * 80)
        code = input(
            'Digite a descrição ou código da cor: ').strip().capitalize()
        print('=' * 80)
        print()
        
        # Adicionar par ao dict "dict[key] = value"
        color_dict[color] = code
    
    # Modificar descrição da cor
    elif option == '2':
        print('=' * 80)
        change = input(
            'Digite a cor para modificar descrição: ').strip().capitalize()
        print('-' * 80)
        
        # Iterar usuário "value = input('')"
        if change in color_dict:
            new_code = input('Digite a nova descrição: ').strip().capitalize()
            print('-' * 80)
                
            # Atualizar descrição "dict[key] = value"
            color_dict[change] = new_code
            print('Descrição atualizada.')
            print('=' * 80)
            print()
        else:
            print('Cor não encontrada. Tente novamente.')
            print('=' * 80)
            print()
    
    # Relatório
    elif option == '3':
        print('=' * 80)
        print('Relatório atual:')
        print('-' * 80)
        
        # Iniciar flag contadora "dict = {}"
        letter_count = {}
        
        # Iterar entre as cores "for key in dict.keys()"
        for color in color_dict.keys():
            
            # Fatiar a primeira letra "a = key[0]"
            first_letter = color[0]
            
            # Fazer contagem "dict[key] = dict.get(key, value)"
            letter_count[first_letter] = letter_count.get(first_letter, 0) + 1
        
        # Exibir relatório "for key, value in sorted(dict.items())"
        for key, value in sorted(letter_count.items()):
            print(f'{key}: {value}')
        print('=' * 80)
        print()
    
    # Sair
    elif option == '4':
        print('=' * 80)
        print('Sistema encerrado.')
        print('=' * 80)
        print()
        break

    # Condição para opção
    else:
        print('=' * 80)
        print('Opção inválida. Tente novamente.')
        print('=' * 80)
        print()
                
    # Pausa
    print('=' * 80)
    pause = input('Pressione Enter para continuar.')
    print('=' * 80)
    print()