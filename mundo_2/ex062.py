# Exercício 62 – Super Progressão Aritmética v3.0
# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

prim = int(input("Primeiro termo: "))
raz = int(input("Razão da PA: "))

counter = 1
termo = 0
user = -1
tam = 10

while True:
    while counter < tam:
        termo += raz
        counter += 1
        print(termo)
    user = int(input("Mais termos: "))

    if user == 0:
        break
    user += counter
    tam = user

print("Fim.")
