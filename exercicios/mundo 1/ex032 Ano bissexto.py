# Faça um progama que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisasr o ano atual!: '))
if ano == 0:
    ano = date.today().year  # vai pegar a data de hoje, mas só o ano atual.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # essa formula é para ver se o ano é bissexto independente do ano.
    print('O ano {} é BISSXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
