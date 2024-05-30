# Exercício 36 – Aprovando Empréstimo
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

preco = float(input("Qual o valor da casa? "))
sal = float(input("Qual é o seu salário? "))
tempo = int(input("Em quantos anos você vai pagar? "))

prestação = preco / (tempo * 12)
salario = sal * 0.3

print(f"Valor da casa: R${preco:.2f}")
print(f"Prestação: R${prestação:.2f}")

if prestação > salario:
    print("Empréstimo negado.")
else:
    print(
        f"Empréstimo concedido. prestação durante {tempo} anos: R${prestação:.2f}")
