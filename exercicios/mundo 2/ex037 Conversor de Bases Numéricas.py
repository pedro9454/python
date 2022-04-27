#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))  # aqui o usuário vai digitar um dos números de cima.
if opcao == 1:  # BINÁRIO
    print('{} convertido para BINÁRIO é igula a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:  # OCTAL
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igula a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida. Tente novamente.')
