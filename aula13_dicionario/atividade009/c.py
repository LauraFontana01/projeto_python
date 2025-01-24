# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 16/01/2025
# # Crie um dicionário iterável com 5 ferramentas.
# Nome da ferramenta: chave, valor: descrição ou especificação técnica dessa ferramenta. 
# Opção de alterar valor de ferramenta já inserida.
# Imprimir valores de cada ferramenta.
# Imprimir a quantidade total de elementos presentes no dicionário. 
# Listar todas as ferramentas armazenadas e descrições, ordenadas alfabeticamente por nome. 
# Fornecer um relatório com a quantidade de ferramentas que têm mais de uma palavra no nome.

import os


os.system('cls')

# Título
print('-' * 50)
print('DICIONÁRIO DE FERRAMENTAS')
print('-' * 50)
print()

# Dict "dict = {}"
tools_dict = {}

# Iterar 5 ferramentas "for i in range(value)"
for i in range(5):
    name = input(f'Nome da {i + 1}ª ferramenta: ').strip().capitalize()
    print('-' * 50)
    description = input(
        f'Descrição da {i + 1}ª ferramenta: ').strip().capitalize()
    print('-' * 50)
    print()
    
    # Adicionar par cor-código ao dict "dict[key] = value"
    tools_dict[name] = description

# Looping Menu "while True"
while True:
    
    # Limpar Terminal
    os.system('cls')
    
    # Ordenar dict pela chave "dict_2 = sorted(dict.items())"
    dict_ordem = sorted(tools_dict.items())
    
    # Exibir dict inicial ordenado "for key, value in dict.items()"
    print('-' * 50)
    print('Dicionário atual: ')
    print('-' * 50)
    for key, value in dict_ordem:
        print(f'{key}: {value}')
    print('-' * 50)
    print()
    
    # Menu
    print('-' * 50)
    print('Menu de opções:')
    print('-' * 50)
    print('1. Modificar descrição de uma ferramenta.')
    print('-' * 50)
    print('2. Exibir descrição de ferramenta específica.')
    print('-' * 50)
    print('3. Gerar relatório detalhado.')
    print('-' * 50)
    print('4. Sair.')
    print('-' * 50)
    option = input('Digite uma opção (1-4): ')
    print('=' * 50)
    print()
    
    # Modificar descrição da cor
    if option == '1':
        print('=' * 50)
        change = input(
            'Digite a ferramenta pra modificar sua descrição: '
            ).strip().capitalize()
        print('-' * 50)
        
        # Iterar usuário "value = input('')"
        if change in tools_dict:
            new_description = input(
                'Digite a nova descrição: ').strip().capitalize()
            print('-' * 50)
                
            # Atualizar descrição "dict[key] = value"
            tools_dict[change] = new_description
            print('Descrição atualizada.')
            print('=' * 50)
            print()
        else:
            print('Ferramenta não encontrada. Tente novamente.')
            print('=' * 50)
            print()
    
    # Exibir descrição específica
    elif option == '2':
        print('=' * 50)
        tool_description = input(
        'Digite a ferramenta para ver sua descrição: ').strip().capitalize()
        print('=' * 50)
        print()

        # Condição de existência "if a in dict"
        if tool_description in tools_dict:
            print('=' * 50)
            print(f'Descrição de {tool_description}: {tools_dict[key]}')
            print('=' * 50)
            print()
        else:
            print('=' * 50)
            print('Ferramenta não encontrada.')
            print('=' * 50)
            print()

    # Relatório
    elif option == '3':

        # Exibir dict inicial ordenado "for key, value in dict.items()"
        print('=' * 50)
        print('Dicionário atual: ')
        print('-' * 50)
        for key, value in dict_ordem:
            print(f'{key}: {value}')
        print('=' * 50)
        print()

        # Contar elementos "a = len(dict)"
        total_tools = len(tools_dict)
        print('=' * 50)
        print(f'Quantidade de elementos do dicionário: {total_tools}')
        print('=' * 50)
        print()

        # Identificar ferramentas com mais de uma palavra "a = [key for key in dict.keys if len(key.split()) > 1]"
        multi_tool_words = [
            key for key in tools_dict.keys() if len(key.split()) > 1]

        print('=' * 50)
        print(f'Quantidade de ferramentas com mais '
              f'de uma palavra no nome: {len(multi_tool_words)}.')
        print('=' * 50)
        print()

    # Sair
    elif option == '4':
        print('=' * 50)
        print('Sistema encerrado.')
        print('=' * 50)
        print()
        break

    # Condição para opção
    else:
        print('=' * 50)
        print('Opção inválida. Tente novamente.')
        print('=' * 50)
        print()
                
    # Pausa
    print('=' * 50)
    pause = input('Pressione Enter para continuar.')
    print('=' * 50)
    print()