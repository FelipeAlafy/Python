valor = input('Digite qualquer coisa e eu vou indentificala > ')
print("\033[31m--------------------------\n"
      "     Indentificando\n"
      "--------------------------\033[m")
print("O tipo é {}\nAlpha Númerio {}\nAlfabeto {}\nTabela Ascii {}\nEm caixa alta {}\nDecimal {}\nDigito {}\nCaixa baixa"
      " {}\nIntificavel {}\nNúmerico {}\nImprimivel {}\nEspaço {}\nTitulo {}".format(type(valor), valor.isalnum(), valor.isalpha(),
      valor.isascii(), valor.isupper(), valor.isdecimal(),
      valor.isdigit(), valor.islower(), valor.isidentifier(), valor.isnumeric(), valor.isprintable(), valor.isspace(),
      valor.istitle()))
