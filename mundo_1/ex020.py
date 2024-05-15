# Exercício 20 – Sorteando uma ordem na lista
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# A função random.shuffle(lista) embaralha os elementos de uma lista fornecida.
from random import shuffle

a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'O nome da lista em ordem dos alunos sorteados são: {lista}')
