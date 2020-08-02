frase = str(input("Digite uma frase qualquer: "))
A = frase.count('A')
Ap = frase.find('A')
Aup = frase.rfind('A')
print("""A letra \"A\" aparece {} vezes na frase.
A primeira posição em que ela aparece é em {}.
A última possiçãp em que ela aparece é em {}.""".format(A, Ap, Aup))
