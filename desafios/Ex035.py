r1 = int(input("Digite a primeira reta: "))
r2 = int(input("Digite a segunda reta: "))
r3 = int(input("Digite a terceira reta: "))

# Verificando qual é a maior reta. E calculando.
if r1 > r2 and r1 > r3:
    maior = r1
    if r2 + r3 > r1:
        formaTriangulo = "SIM"
    else:
        formaTriangulo = "NÃO"
else:
    if r2 > r3:
        maior = r2
        if r1 + r3 > maior:
            formaTriangulo = "SIM"
        else:
            formaTriangulo = "NÃO"
    else:
        maior = r3
        if r1 + r2 > maior:
            formaTriangulo = "SIM"
        else:
            formaTriangulo = "NÃO"

# Exibindo o resultado
print("É possível formar um triângulo com r1 = {}, r2 = {}, r3 = {}? {} é possível.".format(r1, r2, r3, formaTriangulo))
