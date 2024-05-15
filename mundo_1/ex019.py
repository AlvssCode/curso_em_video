# Exercício 19 – Sorteando um item na lista
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

# A função random.choice(lista) retorna um elemento aleatório de uma lista fornecida.
from random import choice

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

escolhido = choice([a1, a2, a3, a4])

print(f"O aluno escolhido é: {escolhido}")
