# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 29/01/2025
# Tratamento de erros

# ZeroDivisionError
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print('Erro: Divisão por zero!')

# ValueError
try:
    numero = int('não é um número')
except ValueError:
    print('Erro: Valor não inválido!')

# TypeError
try:
    soma = '5' + 5
except TypeError:
    print('Erro: Tipo de dado incompatível!')

# IndexError
lista = [1, 2, 3]
try:
    item = lista[5]
except IndexError:
    print('Erro: Índice fora do intervalo da lista!')

# KeyError
dicionario = {'chave': 'valor'}
try:
    valor = dicionario['chave_inexistente']
except KeyError:
    print('Erro: chave não encontrada no dicionário!')

# FileNotFoundError
try:
    with open('arquivo_inexistente.txt', 'r') as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado!')

    # Falta + coisas