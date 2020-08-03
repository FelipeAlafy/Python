"""nome = input("Qual seu nome? ")
if nome == "Felipe":
    print("Que nome lindo você tem!!!")
print("Bom dia! {}".format(nome))"""

n1 = int(input("1ª nota: "))
n2 = int(input("2ª nota: "))
m = (n1 + n2)/2
print("Sua média foi {}".format(m))
if m >= 6.0:
    print("Sua média foi boa PARABÉNS!")
else:
    print("Estude mais!")
