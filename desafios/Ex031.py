km = int(input("De quantos km é a viagem? "))
if km <= 200:
    print("O preço da viagem fica em R${}.".format(km * 0.50))
else:
    print("O preço da viagem fica R${}.".format(km * 0.50))
