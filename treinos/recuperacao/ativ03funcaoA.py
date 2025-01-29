# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Recuperação Funções

# º Receber número - OK
# º Imprimir raiz quadrada do número.
# º Arredondar as raízes pra cima ou pra baixo.
# º Validar números negativos.
# º Avisar ao usuário que o resultado será um número complexo.

import os 
import math


os.system('cls')

# Função calcular raiz quadrada
def calcular():
    raizquadrada = math.sqrt(numero) # função math.sqrt(x) retorna a raiz quadrada de um número x. O valor de x deve ser positivo!
    return raizquadrada

# Função validação - verificar se um número fornecido atende a certos critérios ou condições predefinidas
def validar():
    if numero > 0:
        arredondar_acima = math.ceil(raizquadrada) # função math.ceil(x) retorna o menor número inteiro maior ou igual a x. Ela arredonda o número para cima, para o próximo inteiro.
        return arredondar_acima
    else:
        print('Número ínvalido. Digite outro número!')

# Entrada usuário número
numero = float(input('Insira um número: '))

# Programa principal
raizquadrada = math.sqrt(numero)
arredondar_acima = math.ceil(raizquadrada)


# Saída funçôes
print(f'A raiz quadrada de {numero} é {arredondar_acima}!')