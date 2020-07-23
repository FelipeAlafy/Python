n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

s = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
exp = n1 ** n2
rdiv = n1 % n2
divi = n1 // n2

print('a soma é {}, a subtração é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s, sub, mult, div), end=' >>> ')
print('a exponenciação é {}, o resto da divisão é {}, e a divisão inteira é {}'.format(exp, rdiv, divi))
