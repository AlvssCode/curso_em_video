# Exercício 70 – Estatísticas em produtos
# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

soma_total = 0
contagem_produtos_caros = 0
preco_menor = 0
produto_mais_barato = ''

while True:
    item = input('Digite o nome do item: ')
    valor = float(input('Valor: R$'))
    soma_total += valor
    if valor > 1000:
        contagem_produtos_caros += 1
    if preco_menor == 0 or valor < preco_menor:
        preco_menor = valor
        produto_mais_barato = item
    prosseguir = input('Deseja prosseguir? [S/N] ')
    if prosseguir in 'Nn':
        break

print(f'O valor total da compra foi R${soma_total:.2f}')
print(f'Temos {contagem_produtos_caros} produtos com valor superior a R$1000.00')
print(
    f'O item mais barato foi {produto_mais_barato} que custa R${preco_menor:.2f}')
