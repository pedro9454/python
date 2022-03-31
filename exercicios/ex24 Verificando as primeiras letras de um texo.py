# Crie um progama que leia o nome de uma cidade se ela COMEÇA ou não com o nome "SANTO"

cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[0:5].lower() == 'santo')

# strip() = tira os espaçoes desnecessarios
# upper() = joga todas as letras para maiúsculas
# lower() = joga todas as letras para minúsculas

