arquivo = open('emails.txt','r')
saida2= open('arquivo.txt', 'w')
with arquivo as arq:
    for i in arq.read().lower().split():
        if i.find(r'@')>-1:
            saida2.write(i)
            saida2.write()



