# Crie um progama que leia o nome de uma cidade se ela COMEÇA ou não com o nome "SANTO"

cid = str(input('Digite onde você nasceu: ')).strip()
print(cid[0:5].upper() == 'SANTO')

