# Exercício 16 – Quebrando um número
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# trunc() do módulo math remove a parte fracionária de um número, retornando apenas a parte inteira.
from math import trunc

num = float(input("Digite um número real: "))
inteiro = trunc(num)

print(f"O valor digitado foi {num} e a sua porção inteira é {inteiro}.")
