# Crie um programa que leia um número real e mostre sua parte inteira
from math import floor
value = float(input("Qual o valor? "))
value = floor(value)
print("\033[32mA parte inteira desse valor é {}.".format(value))
