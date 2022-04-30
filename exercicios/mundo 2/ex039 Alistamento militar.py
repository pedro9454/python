# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date  # vamos usar essa biblioteca paga pegar o ano atual que está no seu computador.
atual = date.today().year  # é para saber o ano de hoje que está no seu computador.
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento  # calcular a idade pega o ano atual e subitrai com o ano de nascimento.
sexo = str(input('Sexo: '))


# PRIMEIRA PARTE
if sexo == 'Feminino':
    print('Você não precisa fazer o alistamento militar obrigatório.')
elif sexo == 'Masculino':
    print('Você precisa fazer o alistamento militar obrigatório.')
    print('Quem nasceu em {} tem {} anos em {}. Siga as orientações abaxo:'.format(nascimento, idade, atual))

# SEGUNDA PARTE
if sexo == 'Masculino' and idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif sexo == 'Masculino' and idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {} ano.'.format(ano))

elif sexo == 'Masculino' and idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {} ano.'.format(ano))




