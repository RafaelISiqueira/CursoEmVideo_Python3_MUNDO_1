#Nome completo de uma pessoa: 1: Maiúsculas, 2: Minúsculas, 3:Quantas letras no total, 4:quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip() #strip() para eliminar espaços
print('----------------------------------------------------------------')
print('Seu nome é {}'.format(nome))
print('Seu nome em Maiúsculo fica: {}.'.format(nome.upper()))
print('Seu nome em Minúsculo fica: {}.'.format(nome.lower()))
print('Seu nome tem ao todo: {} Letras.'.format(len(nome) - nome.count(' ')))
#print('O seu primeiro nome tem: {} Letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} Letras.'.format(separa[0], len(separa[0])))
