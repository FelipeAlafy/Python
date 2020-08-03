from random import randint
print("Vou pensar em um número entre 0 e 5 tente adivinhar!!")
computador = randint(0, 5)
player = int(input("Qual é o seu chute? "))
if player == computador:
    print("PARABÉNS! Você venceu pois advinhou meu pensamento!\nplayer: {},\ncomputador {}.".format(player, computador))
else:
    print("Você perdeu pois você disse {}\nQuando na verdade eu pensei em {}.".format(player, computador))
