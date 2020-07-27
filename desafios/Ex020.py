# O mesmo professor quer sortear a ordem de apresentação dos seus alunos. Faça um programa para ajuda-lo.
from random import shuffle
aluno1 = input("Qual o primeiro aluno? ")
aluno2 = input("Qual o segundo aluno? ")
aluno3 = input("Qual o terceiro aluno? ")
aluno4 = input("Qual o quarto aluno? ")
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print("A ordem deve ser {}.".format(lista))
