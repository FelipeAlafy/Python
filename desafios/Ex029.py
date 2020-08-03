vel = int(input("Qual a velocidade atual? "))
if vel > 80:
    multa = vel - 80
    multa = multa * 7
    print("\033[31mVocê foi multado em R${}.".format(multa))
else:
    print("\033[32mDirija com segurança!!")








