ano = int(input("Digite um ano qualquer: "))
if ano % 4 == 0 and ano % 100 != 0:
    print("O ano {}, é BISSEXTO!".format(ano))
else:
    print("O ano {}, NÃO é BISSEXTO!".format(ano))
