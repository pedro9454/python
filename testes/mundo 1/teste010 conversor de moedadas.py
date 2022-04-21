real = float(input('Digite um valor: R$'))
dolar = real / 5.01
iene = real / 0.043
euro = real / 5.51
print('Com tantos R${} você pode comprar \nU${:.2f} \n¥{:.2f} \n€{:.2f}'.format(real, dolar, iene, euro))
