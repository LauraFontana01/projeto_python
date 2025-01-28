# Curso Técnico em Desenvovimentos em Sistemas 
# Turma 0392
# Autor: Laura Fontana
# Professor: Sebastião Marcos
# Data: 02/12/2024
# Atividade 008

import os


os.system('cls')

# Conjunto secreto definido
conjunto_secreto = {'2', '4', '6', '8'}

# Entrada do jogo
print('-'*50)
print("Bem-vindo ao jogo de adivinhação de conjunto :)\nDica: O conjunto contém 4 números de 0 a 10. Tente adivinhar os números!")
print('-'*50)

# Loop para permitir múltiplas tentativas
while True:
    # Entrada do jogador
    entrada = input("Digite os números separados por vírgulas: ").strip().lower()
    print('-'*50)
    adivinhacao = set(entrada.split(","))
    
    # Removendo os espaços extras em cada item
    adivinhacao = {item.strip() for item in adivinhacao}

    # Verificar diferenças
    faltando = conjunto_secreto.difference(adivinhacao)
    extras = adivinhacao.difference(conjunto_secreto)

    # Feedback para o jogador
    if faltando or extras:
        print("\nResultado da sua tentativa:")
        if faltando:
            print(f"Faltando na sua adivinhação: {faltando}")
        if extras:
            print(f"Errados na sua adivinhação: {extras}")
        print("Tente novamente!\n")
    else:
        print("\nParabéns! Você adivinhou corretamente o conjunto secreto:", conjunto_secreto)
        break


