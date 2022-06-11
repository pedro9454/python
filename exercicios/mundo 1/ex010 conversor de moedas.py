real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.99
iene = real / 0.043
euro = real / 5.51
print('Com tantos R${:.2f} você pode comprar: \nUS${:.2f} \n¥{:.2f} \n€{:.2}'.format(real, dolar, iene, euro))




