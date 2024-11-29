




import os


os.system('cls')

# Conjunto secreto definido
conjunto_secreto = {"morango", "banana", "limão", "laranja"}

# Entrada do jogo
print("Bem-vindo ao jogo de adivinhação de conjuntos :) ")
print("Dica: O conjunto contém 4 frutas. Tente adivinhar os elementos!")

# Loop para permitir múltiplas tentativas
while True:
    # Entrada do jogador
    entrada = input("Digite os nomes das frutas separados por vírgulas: ").strip().lower()
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
