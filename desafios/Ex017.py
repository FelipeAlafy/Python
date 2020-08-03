# Faça um programa que leia o cateto oposto, e o cateto adjacente e mostre o valor da hipotenusa
cateto_oposto = float(input("Qual o valor do cateto oposto? "))
cateto_adjacente = float(input("Qual o valor do cateto adjacente? "))
hipotenusa = (pow(cateto_oposto, 2)) + (pow(cateto_adjacente, 2))
print("O valor da hipotenusa em um triângulo retângulo, onde o cateto oposto vale {}^2 que é igual {},\n"
      "e o cateto adjacente vale {}^2 que é igual {}, \033[32ma hipotenusa é igual a {}\033[m".format(cateto_oposto, pow(cateto_oposto, 2),  cateto_adjacente, pow(cateto_adjacente, 2), hipotenusa))
