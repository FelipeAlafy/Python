sal = float(input('Qual é o seu salário atual: '))
nsal = (sal + ((sal * 15) / 100))
print("\033[32mSeu novo salário com 15% de aumento é de R${:.2f} 🤑".format(nsal))
