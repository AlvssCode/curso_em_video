# Exercício 15 – Aluguel de Carros
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Dias que o carro foi alugado: "))
km = float(input("Digite a quantidade de Km rodados: "))

total = (dias * 60) + (km * 0.15)

print(f"O preço total a pagar é: R${total:.2f}")
