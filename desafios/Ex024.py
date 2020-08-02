cidade = str(input("Qual o nome da sua cidade? ")).strip()
cidade = cidade.split()
santo = 'santo' in cidade[0].lower()
print("O nome da cidade começa com Santo? {}".format(santo))
