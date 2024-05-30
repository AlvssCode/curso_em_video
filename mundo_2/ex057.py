# Exercício 57 – Validação de Dados
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input("Digite o seu sexo (M ou F): ").strip().upper()[0]

while sexo not in ['M', 'F']:
    print("Entrada inválida. Por favor,Digite o seu sexo (M ou F).")
    sexo = input("Digite o seu sexo (M ou F): ").strip().upper()[0]

print("Sexo registrado com sucesso: " + sexo)
