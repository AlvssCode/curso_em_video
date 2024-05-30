
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))


imc = peso / (altura ** 2)

if imc < 18.5:
    status = 'Abaixo do Peso'
elif 18.5 <= imc < 25:
    status = 'Peso Ideal'
elif 25 <= imc < 30:
    status = 'Sobrepeso'
elif 30 <= imc < 40:
    status = 'Obesidade'
else:
    status = 'Obesidade Mórbida'

print(f'Seu IMC é {imc:.2f}')
print(f'Seu status é: {status}')
