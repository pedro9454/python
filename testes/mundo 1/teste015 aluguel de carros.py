dias = int(input('Quantos dias aludo? '))
km = float(input('quantos km rodados? '))
pago = (60 * dias) + (0.15 * km)
print('O total a pagar será de {:.2f}'.format(pago))
