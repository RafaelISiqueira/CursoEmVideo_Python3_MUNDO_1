# Calculo de novo salário: para valores > R$1.250,00 calcule 10%. para os inferiores o aumento é de 15%.
salário = float(input('Qual é o sálario do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100) # 15 / 100 = 15%
else:
    novo = salário + (salário * 10 / 100 )# 10 / 100 = 10%
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário, novo))
