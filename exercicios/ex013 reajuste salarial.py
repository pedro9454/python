salario = float(input('Qual é o salario do Funcionário? R$'))
novo = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, novo))
