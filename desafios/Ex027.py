nome = str(input("Digite o seu nome completo: ")).strip()
nome = nome.split()
pnome = nome[0]
unome = nome[len(nome)-1]
print("\033[31mSeu primeiro nome é {}".format(pnome))
print("\033[36mSeu último nome é {}".format(unome))
