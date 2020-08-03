num = int(input("Digite um número entre 0 e 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("\033[36munidade: {}\033[m".format(u))
print("\033[33mdezena:  {}\033[m".format(d))
print("\033[32mcentena: {}\033[m".format(c))
print("\033[31mmilhar:  {}\033[m".format(m))
