#Calculando Descontos
n = float(input('Seu produto, terá 5% de desconto, digite seu valor: '))
d = n*0.05
r = n - d
print('Valor original: R${:.2f}, Valor do desconto de 5%: R${:.2f}! Valor depois do ajuste : R${:.2f}.'.format(n, d, r))

