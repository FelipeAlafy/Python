v = float(input("Digite o valor do produto para aplicar o desconto: "))
desc = (v - (v * 5 / 100))
print("O desconto de 5% fora aplicado 😁 e o preço agora é de R${:.2f}".format(desc))