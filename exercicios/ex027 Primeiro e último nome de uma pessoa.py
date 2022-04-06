# Faça um progama que leia o nome completo de uma pessoa, mostrando em seguida o promeiro e ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
separa = nome.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}'.format(separa[0]))
print('Seu último nome é {}'.format(separa[len(separa)-1]))

# len() = mostra quantas posições tem a variavel
# split() = separa a string em lista

