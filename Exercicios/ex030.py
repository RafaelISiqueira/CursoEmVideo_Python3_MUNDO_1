# criar um programa que leia um numero e dizer se ele é par ou impar
num = int(input('Me diga um número qualquer: '))
# qualquer numero dividido por 2 é (par)
resultado = num % 2
if resultado == 0:
    print('O numero {} PAR!'.format(num))
else:
    print('O numero {} ÍMPAR'.format(num))
