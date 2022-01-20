#Dissecando uma variável
n = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é:', type(n))
print('Apenas letras?', n.isalpha())
print('é um Espaço?', n.isspace())
print('é um numero decimal?', n.isdecimal())
print('Possue letra Maiuscula?', n.isupper())
print('Possue letras minusculas?', n.islower())
