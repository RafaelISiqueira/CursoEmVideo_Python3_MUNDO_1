#mostrar que o nome de uma pessoa conteum ''Silva'' no nome
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva?: {}'.format('SILVA'in nome.upper()))
#botar para miuscula para evitar letras Minusculas e Maiusculas.