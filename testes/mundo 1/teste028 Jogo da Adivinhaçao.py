# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
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
