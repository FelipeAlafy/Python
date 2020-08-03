v1 = int(input("Digite um número: "))
v2 = int(input("Digite outro número: "))
v3 = int(input("Digite o último número: "))
# verificando o maior
if v1 > v2 and v1 > v3:
    maior = v1
else:
    if v2 > v3:
        maior = v2
    else:
        maior = v3

# verificando o menor
if v2 > v1 and v3 > v1:
    menor = v1
else:
    if v3 > v2:
        menor = v2
    else:
        menor = v3

print("\033[34mO maior número é {}".format(maior))
print("\033[33mO menor número é {}".format(menor))
