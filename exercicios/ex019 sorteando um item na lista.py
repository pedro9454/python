import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]  # Uma lista fica entre couchettes
escolhido = random.choice(lista)  # O choice() = escolhe um valor
print('O aluno escolhido foi {}'.format(escolhido))

# Uma lista fica entre couchettes
# O choice() = escolhe um valor


