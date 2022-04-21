# Escreva um progama que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma menssagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você excedeu o limite de velocidade permitido da via, que é de 80Km/h.')
    multa = (velocidade - 80) * 7.00
    print('Você terá que pagar uma multa de {:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com cuidado!')
