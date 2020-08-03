dias = int(input("Quantos dias você ficou com o carro? "))
km = float(input("Quantos KM você rodou com o carro? "))
res = (dias * 60) + (km * 0.15)
print("\033[31mO total a pagar pelo carro é R${:.2f}🤑🤑🤑".format(res))
