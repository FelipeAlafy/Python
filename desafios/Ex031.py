km = int(input("De quantos km é a viagem? "))
if km <= 200:
    print("\033[31mO preço da viagem fica em R${}.".format(km * 0.50))
else:
    print("\033[32mO preço da viagem fica R${}.".format(km * 0.45))
