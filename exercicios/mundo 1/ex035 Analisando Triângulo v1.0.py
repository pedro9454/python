# Desenvolva um progama que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
# regra matemática: Cada um dos seguimentos tem que ser menor que a soma dos outros dois seguimentos.
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR um triângulo!')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo!')

