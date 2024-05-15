# Exercício 24 – Verificando as primeiras letras de um texto
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input("Digite o nome de uma cidade: ")
print(f"A cidade começa com 'SANTO'? {cidade.upper().startswith('SANTO')}")
