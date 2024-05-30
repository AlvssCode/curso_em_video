# Exercício 40 – Aquele clássico da Média
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    situacao = 'REPROVADO'
elif 5.0 <= media <= 6.9:
    situacao = 'RECUPERAÇÃO'
else:
    situacao = 'APROVADO'

print(f'Média: {media:.1f}')
print(f'Situação: {situacao}')
