# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 23/01/2025
# Crie uma função que receba uma temperatura em fahrenheit e retorne o valor em graus célsius.

import os


os.system('cls')

# Título
print('-'*50)
print('Função de conversão °F para °C')
print('-'*50)

# Definição da função chamada de "temperatura" recebe parâmetro "fahrenheit"
# Definir função "def function(param)"
def temp(fahrenheit):
    # Converção fahrenheit -> celsius
    celsius = (fahrenheit - 32) / 9 * 5 
    return celsius

# Entrada do usuário
fahrenheit = int(input('Digite a temperatura em fahrenheit: '))
print('-'*50)

# Invocação da função - "a = function(argument)"
tempcelsius = temp(fahrenheit)

# Saída
print(f'Conversão de {fahrenheit}°F para célsius: {tempcelsius:.2f}°C')
print('-'*50)