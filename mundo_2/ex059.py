# Exercício 59 – Criando um Menu de Opções
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

menu = (
    '''MENU PRINCIPAL:
[1] Adição
[2] Multiplicação
[3] Comparação
[4] Inserir novos números
[5] Sair do programa'''
)

print(menu)

opcao_usuario = int(input("Escolha uma opção (de 1 a 5): "))
while opcao_usuario != 5:
    if opcao_usuario > 5:
        print("Atenção: escolha um número de 1 a 5.")
        opcao_usuario = int(input("Escolha uma opção: "))
    elif opcao_usuario < 0:
        print("Atenção: escolha um número positivo.")
        opcao_usuario = int(input("Escolha uma opção: "))
    else:
        if opcao_usuario == 1:
            print(f"Você escolheu adição! Resultado da adição: {primeiro_numero} + {segundo_numero} = {primeiro_numero + segundo_numero}")
            print(menu)
            opcao_usuario = int(input("Escolha uma opção: "))
        elif opcao_usuario == 2:
            print(f"Você escolheu multiplicação! Resultado da multiplicação: {primeiro_numero} x {segundo_numero} = {primeiro_numero * segundo_numero:.0f}")
            print(menu)
            opcao_usuario = int(input("Escolha uma opção: "))
        elif opcao_usuario == 3:
            if primeiro_numero > segundo_numero:
                print(f"O maior número é {primeiro_numero} e o menor número é {segundo_numero}.")
                print(menu)
            elif segundo_numero > primeiro_numero:
                print(f"O maior número é {segundo_numero} e o menor número é {primeiro_numero}.")
                print(menu)
            else:
                print("Os dois números são iguais.")
                print(menu)
            opcao_usuario = int(input("Escolha uma opção: "))
        elif opcao_usuario == 4:
            primeiro_numero = float(input("Digite o novo primeiro número: "))
            segundo_numero = float(input("Digite o novo segundo número: "))
            print(menu)
            opcao_usuario = int(input("Escolha uma opção: "))
print("Opção 5: programa encerrado.")
