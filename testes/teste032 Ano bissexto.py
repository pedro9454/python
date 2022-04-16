# Faça um progama que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano quer analisar? '))
if ano == 0:  # Se for digitado o número 0 vai está sendo represendo o ano atual do seu computador
    ano1 = date.today().year  # Vai mostrar o ano atual que está no configurado no seu pc
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!')
else:
    print('O ano {} não é BISSEXTO!')

