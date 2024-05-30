# Exercício 61 – Progressão Aritmética v2.0
# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

decimo_termo = primeiro_termo + (10 - 1) * razao

termo_atual = primeiro_termo
while termo_atual <= decimo_termo:
    print(f"{termo_atual}")
    termo_atual += razao
