# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# – O nome com todas as letras maiúsculas e minúsculas.
#
# – Quantas letras ao todo (sem considerar espaços).
#
# – Quantas letras tem o primeiro nome.
nome = str(input('Digite seu noem completo: ')).strip()  # strip = elimina os espaços desnecessarios
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu noem tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
# print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))

# strip = elimina os espaços desnecessarios
# upper = muda as letras para maiúsculas
# lower = muda as letras para minúsculas
# lean = conta quantos caracteres tem na string
# count = conta quantas coisas que foram colocadas em parenteses



