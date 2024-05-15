# Exercício Python 12 – Calculando Descontos
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input("Digite o preço do produto: "))
desconto = (preço * 5 / 100)
novo = preço - desconto
print(f"O preço do produto com 5% de desconto é: {novo:.2f}")
