# Exercício 63 – Sequência de Fibonacci v1.0
# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
#  Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

n = int(input("Termos:"))
t1, t2 = 0, 1
print(f"{t1} > {t2}", end="")
cont = 3
while cont <= n:
    t1, t2 = t2, t1 + t2
    print(f" > {t2}", end="")
    cont += 1
print(" > Fim!")
