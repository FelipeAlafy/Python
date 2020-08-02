nome = str(input("Digite o seu nome completo: ")).strip()
nome = nome.split()
pnome = nome[0]
unome = nome[len(nome)-1]
print("Seu primeiro nome é {}".format(pnome))
print("Seu último nome é {}".format(unome))
