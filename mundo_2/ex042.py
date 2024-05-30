# Exercício 42 – Analisando Triângulos v2.0
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

a = float(input("Primeiro segmento de reta: "))
b = float(input("Segundo segmento de reta: "))
c = float(input("Terceiro segmento de reta: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        tipo = "EQUILÁTERO"
    elif a == b or b == c or a == c:
        tipo = "ISÓSCELES"
    else:
        tipo = "ESCALENO"
    print(f"O triângulo que existe é um triângulo {tipo}.")
else:
    print("Os segmentos não podem formar um triângulo.")
