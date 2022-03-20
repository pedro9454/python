preço = float(input('Qual é o preço do produto? R$'))
desconto = preço - (preço * 8 / 100)
print('O produto que custava R${} com o desconto de 5% vai custar R${:.2f}'.format(preço, desconto))
