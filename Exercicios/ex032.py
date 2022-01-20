#ano bissexto: diga se o ano é bissexto ou não.
ano = int(input('Que ano quer analisar? '))
# exceto anos multiplos de 100 que não são multiplos de 400 (google)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É UM ANO BISSEXTO'.format(ano))
