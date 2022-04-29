# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais
n1 = int(input('PRIMERO número: '))
n2 = int(input('SEGUNDO número: '))
if n1 > n2:
    print('O \033[0;36mPRIMEIRO\033[m valor é maior!')
elif n2 > n1:
    print('O \033[0;32mSEGUNDO\033[m valor é meior!')
else:
    print('Não existe valor maior, os dois são iguais!')
