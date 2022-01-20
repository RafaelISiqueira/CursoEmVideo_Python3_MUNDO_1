#leia o nome de uma cidade, e diga, se ela começa ou não com ''santo''
local = str(input('Em qual cidade Você nasceu: ')).strip()
print(local[:5].upper() == 'SANTO')
# joga tudo para maiusculo
