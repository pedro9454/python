# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: ').strip())
idade = atual - nascimento
sexo = str(input('Sexo: ').upper().strip())

if sexo == 'FEMININO':
    print('Você não precisa fazer o alistamento militar obrigatório.')
elif sexo == 'MASCULINO':
    print('Você precisa fazer o alistamento militar obrigatório. Siga as orientações abaixo:')
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, atual))


if sexo == 'MASCULINO' and idade == 18:
    print('Você tem que fazer o alistamento IMEDIATAMENTE!')
elif sexo == 'MASCULINO' and idade < 18:
    saldo = 18 -idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento vai se em {} anos'.format(ano))
elif sexo == 'MASCULINO' and idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))








