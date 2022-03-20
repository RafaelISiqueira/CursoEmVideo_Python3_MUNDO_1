#leia o nome completo da pessoa e mostre o primeiro e o ultimo nome separadamente
#ex. ana maria da silva pereira primeiro = ana, ultimo = pereira
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito Prazer em te conhecer!')
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu Último nome é: {}'.format(nome[len(nome)-1]))

