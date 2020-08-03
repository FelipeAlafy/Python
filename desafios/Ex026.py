frase = str(input("Digite uma frase qualquer: ")).strip().upper()
A = frase.count('A')
Ap = frase.find('A')+1
Aup = frase.rfind('A')+1
print("""\033[35mA letra \"A\" aparece {} vezes na frase.
A primeira posição em que ela aparece é em {}.
A última posição em que ela aparece é em {}.""".format(A, Ap, Aup))
