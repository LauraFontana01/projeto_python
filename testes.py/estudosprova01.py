# Autor: Laura Fontana
# Data: 30/10/2024
# Estudos pra provuska de amanhã
# Quando tempo você demora para percorrer 183km até o RJ? Peça ao usuário para inserir quantos km ele caminha e calcule 
# quantas horas e dias você demoraria para chegar no RJ a 183km/h daqui andando x km/h?

import os 


os.system('cls')

print('~'*50)
print('Quanto tempo você demoraria pra chegar no RJ a pé?')
print('='*50)


km = float(input('Quantos KM/h você percorre?: ')) # Inserir km/h andando e comparar com 183km/h pro RJ

dia = 24 # horas
km_1 = 183 # metros


viagem = (km_1) % (km) # o resultado
km_2 = 


print(f' Você vai andar {viagem:.2f} km/h e vai demorar {dia} dias pra chegar no RJ ')


