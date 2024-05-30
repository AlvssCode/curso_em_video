# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.


numero = int(input("Informe um número para verificar se é primo: "))

primo = True

limite = (numero // 2)


for divisor in range(limite, 0, -1):
    if numero % divisor == 0 and divisor != 1:
        primo = False


if primo:
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
