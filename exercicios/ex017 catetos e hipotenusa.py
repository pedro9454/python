# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimentpo do cateto adjacente: '))
hi = math.hypot(co, ca)  # hypot = faz o calculo da hipotenusa
print('A hipotenusa vai medir {:.2f}'.format(hi))

# hypot = faz o calculo da hipotenusa