#preço de passagem: pergunte a distancia, calcule o preço da passagem 0,50 o Km e acima de 200km 0,45.
distância = float(input('Qual é a distância da sua viagem? '))
print('Você esta preste a começar uma viagem de {}Km.'.format(distância))
if distância <= 200:
    preço = distância * 0.50 #distancia multiplicada pelo valor
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
