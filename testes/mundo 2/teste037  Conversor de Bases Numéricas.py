# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma base de converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print('{} convertido par BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igula a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igula a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')




