num = str(input("Digite um número entre 0 e 9999: "))
valor = num[0:4]
print("unidade: {}".format(valor[3]))
print("dezena:  {}".format(valor[2]))
print("centena: {}".format(valor[1]))
print("milhar:  {}".format(valor[0]))
