import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimentpo do cateto adjacente: '))
hi = math.hypot(co, ca)  # hypot = faz o calculo da hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))

# hypot = faz o calculo da hipotenusa