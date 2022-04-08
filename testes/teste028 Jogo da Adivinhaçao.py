from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Qual o número que eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('PARABENS! Você acertou o número que eu pensei!')
else:
    print('EU GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))
