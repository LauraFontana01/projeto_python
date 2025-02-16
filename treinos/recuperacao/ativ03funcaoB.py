# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Recuperação Funções

# ª Receba 2 valores
# ª Faça a divisão entre eles. 
# ª Se a divisão não for inteira, o programa deverá arredondar o resultado para cima e para baixo. 
# ª Faça a validação para divisão por 0.

import os
import math

os.system('clear')

# Função calcular divisão
def calcular():
    divisao = numerox / numeroy
    return divisao

# Função validação - verificar se um número fornecido atende a certos critérios ou condições predefinidas
def validar():
    if divisao < 0:
        arredondar_abaixo = math.floor(divisao) # math.floor(x)Retorna o inteiro menor ou igual a x (arredonda para baixo). # função math.ceil(x) retorna o menor número inteiro maior ou igual a x. Ela arredonda o número para cima, para o próximo inteiro.
        return arredondar_abaixo
    else:
        print('Número ínvalido. Digite outro número!')


# Entrada usuário números
numerox = float(input('Digite um número: '))
numeroy = float(input('Digite outro número: '))

# Programa principal
divisao = numerox / numeroy
arredondar_abaixo = math.floor(divisao)

# Saída funções
print(f'A divisão entre {numerox} e {numeroy} é {arredondar_abaixo}')