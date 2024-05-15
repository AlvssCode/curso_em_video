# Exercício 6 – Dobro, Triplo, Raiz Quadrada
# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada

num = int(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print(f"O dobro do número {num} é: {dobro}.")
print(f"O triplo do número {num} é: {triplo}.")
print(f"A raiz quadrada do número {num} é: {raiz:.2f}.")
