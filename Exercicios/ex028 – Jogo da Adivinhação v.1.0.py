#Computador vai pensar em um numero de 0 a 5, e voce tenta advinhar, venceu ou perdeu.
from random import randint
from time import sleep # Pausa para o computador pensar em segundos.
computador = randint(0, 20) # faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 20. Tente Advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número em pensei? '))  # Jogador tenta advinhar
sleep(2)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
