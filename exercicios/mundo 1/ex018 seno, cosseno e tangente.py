# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo {} tem o SENO de {:.2f}'.format(ângulo, seno))
coseno = math.cos(math.radians(ângulo))
print('O ângulo {} tem o COSENO de {:.2f}'.format(ângulo, coseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ângulo, tangente))

