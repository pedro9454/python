# Crie um progma que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número: '))
resultado = numero % 2
if resultado == 0:
    print('O número é par!')
else:
    print('O númeor é impar!')

# O resto da divisão inteira de qualquer número par por dois é zero.
# O resto da divisão inteira de qualquer número ímpar por dois é um.


