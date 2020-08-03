nome = str(input("Digite seu nome completo? ")).strip()
silva = 'silva' in nome.lower()
print("\033[34mSeu nome tem Silva? {}".format(silva))
