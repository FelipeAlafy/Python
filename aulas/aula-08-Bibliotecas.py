from math import sqrt, floor
import random
num = int(input("digite um valor: "))
raiz = sqrt(num)
print("A raiz {} é igual a {:.2f}".format(num, floor(raiz)))

num2 = random.randint(1, 10)
print("\n\nGerando um número aleatório entre 1 e 10")
print("O valor gerado foi {}".format(num2))
