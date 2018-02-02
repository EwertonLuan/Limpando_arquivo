import re

def limpando (arquivo_entrasa, arquivo_saida, iten_procurar):
    arquivo = open(arquivo_entrasa, 'r')
    saida = open(arquivo_saida, 'w')

    with arquivo as arq:
        f = ''
        for i in arq.read().lower().split():
            if i.find(iten_procurar) > -1:
                i = re.sub('[<>!?;]', ' ', i)
                f += i
        for email in f.split():

            saida.write('\n'+email)









