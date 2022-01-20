#montar uma frase, mostrar quantos 'A' tem nela, qual a posição da primeira vez, qual a posição da ultima vez.
frase = str(input('Digite uma Frase: ')).upper().strip()
print('A letra A aparece {} Vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))