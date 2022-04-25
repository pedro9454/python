# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de finaciamento? '))
prestaçao = casa / (anos * 12)  # É o preço da casa dividido por quantos meses ele vai pagar. Para saber em quantos meses ele vai pagar pega a quantidade de anos que ele quer pagar a casa e multiplica por 12 (que é a quantidade de meses que tem um ano).
minimo = salario * 30 / 100
print('Para pagar uma casa de {:.2f} em {} anos a prestação será de {:.2f}'.format(casa, anos, prestaçao))
if prestaçao <= minimo:
    print('Empréstimo pode ser CONCEDIDO1')
else:
    print('Empréstimo NEGADO!')
