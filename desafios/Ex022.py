nome = input("Qual seu nome completo? ").strip()
print("Seu nome em caixa alta fica: {}".format(nome.upper()))
print("Seu nome em caixa baixa fica: {}".format(nome.lower()))
print("Seu nome tem {} letras ao todo sem espaços.".format(len(nome.replace(" ", ""))))
pnome = nome.split()
print("Seu primeiro nome tem \033[36m{}\033[m letras.".format(len(pnome[0])))
