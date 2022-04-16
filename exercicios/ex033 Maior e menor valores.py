# Faça um progama que leia três números inteiros e mostre qual é o maior e manor número.
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# VERIFICANDO QUEM É O MENOR
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
# VERIFICANDO QUEM É O MENOR
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
