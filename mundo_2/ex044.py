# Exercício 44 – Gerenciador de Pagamentos
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

valor = float(input("Digite o valor do produto: "))

print("[ 1 ] à vista dinheiro/cheque")
print("[ 2 ] à vista no cartão")
print("[ 3 ] 2x no cartão")
print("[ 4 ] 3x ou mais no cartão")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    desconto = (10/100) * valor
    print(
        f"O valor da sua compra de R${valor} vai custar R${valor - desconto:.2f}")
elif opcao == 2:
    desconto = (5/100) * valor
    print(
        f"O valor da sua compra de R${valor} vai custar R${valor - desconto:.2f}")
elif opcao == 3:
    print(f"O valor da sua compra de R${valor} será 2x de R${valor/2:.2f}")
elif opcao == 4:
    parcelas = int(input("De quantas vezes você quer dividir? "))
    juros = (20/100) * valor
    juros_parcela = juros / parcelas
    print(
        f"Sua compra será parcelada em {parcelas}x de R${(valor/parcelas) + juros_parcela:.2f} com juros.")
    print(
        f"Sua compra de R${valor} vai custar R${valor + juros:.2f} no final.")
else:
    print("Opção inválida de pagamento. Tente novamente.")
