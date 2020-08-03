sal = float(input("Qual é o seu salário atual? "))
if sal > 1250:
    aume = 10
else:
    aume = 15
nsal = sal + ((sal * aume)/100)
print("O seu salário era {:.2f}, mas com um aumento de {}% ele passou a ser {:.2f}.".format(sal, aume, nsal))
