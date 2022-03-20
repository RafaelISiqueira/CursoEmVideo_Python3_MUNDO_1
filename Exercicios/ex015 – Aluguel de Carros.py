#aluguel de carros
dia = float(input('Quantos dias alugado? '))
km = float(input('quandos Km rodados? '))
cdia = (dia * 60)
ckm = (km * 0.15)
total = (cdia + ckm)
print('O total a pagar é de R${:.2f}.'.format(total))


