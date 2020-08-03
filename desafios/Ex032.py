from datetime import datetime
now = datetime.now()
anoAtual = now.year
ano = int(input("Digite um ano qualquer, ou 0 para o ano atual: "))
if ano == 0:
    ano = anoAtual

if ano % 4 == 0 and ano % 100 != 0:
    print("O ano {}, é BISSEXTO!".format(ano))
else:
    print("O ano {}, NÃO é BISSEXTO!".format(ano))
