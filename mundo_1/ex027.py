# Exercício 27 – Primeiro e último nome de uma pessoa
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite o nome completo de uma pessoa: ").strip().split()

primeiro = nome[0]
ultimo = nome[-1]

print(f"Primeiro nome: {primeiro}")
print(f"Último nome: {ultimo}")
