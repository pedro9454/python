#  Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
computador = randint(0, 5)  # randint() = faz o computador "PENSAR" na coisa que esta no parenteses
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))  # O jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1)  # sleep() = faz o computador esperar, faz ele meio que dormir por alguns segundos, os segundos são colocados nos parenteses
if jogador == computador:
    print('PARABÉNS! Você conseguil me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))

# randint() = faz o computador "PENSAR" na coisa que esta no parenteses
# sleep() = faz o computador esperar, faz ele meio que dormir por alguns segundos, os segundos são colocados nos parenteses
