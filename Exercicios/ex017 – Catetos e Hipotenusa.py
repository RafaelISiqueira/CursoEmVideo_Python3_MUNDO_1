# comprimento do cateto oposto e do cateto adjacente de um triangulo. calcule e mostre a Hipotenusa.
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
# hi = math.hypot(co, ca) import Math
print('\n*********************\n')
print('Um triangulo com Cateto Oposto de {}\ne Cateto Adjacente de {}\nSua hipotenusa vai ser de {}'
      .format(co, ca, hipotenusa))

