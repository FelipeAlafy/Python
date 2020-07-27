# Um professor quer sortear um dos seus quatro alunos(as) para apagar o quadro. Faça um programa para ajudar ele.
from random import choice
aluno1 = input("Nome do primeiro aluno(a)? ")
aluno2 = input("Nome do segundo aluno(a)? ")
aluno3 = input("Nome do terceiro aluno(a)? ")
aluno4 = input("Nome do quarto aluno(a)? ")
lista = [aluno1, aluno2, aluno3, aluno4]
print("O aluno(a) escolhido(a) foi {}.".format(choice(lista)))
