# Exercício 14 – Conversor de Temperaturas
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (1.8 * celsius) + 32
print(f"{celsius:.0f}ºC correspondem a {fahrenheit:.1f}ºF.")
