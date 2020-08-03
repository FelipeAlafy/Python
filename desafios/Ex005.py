n = int(input('Insira um número: '))
print('\033[31mO antecessor é {}, \033[34me o sucessor {}\033[m'.format((n - 1), (n + 1)))
print('Antecessor em emoji> {}, sucessor em emoji> {}'.format(((n - 1) * '✔'), ((n + 1) * '✔')))
