# Exercício 10 – Conversor de Moedas
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

reais = float(input("Digite quantos reais você tem na carteira? R$: "))
USD = 5.12
dollar = reais / USD

print(f"Com R${reais:.2f}, você pode comprar US${USD:.2f}.")
