# Calculadora simples

while True:

    print('\n\t\t\t -- Calculadora -- ')

    print('1. soma')
    print('2. sair')

    op = int(input('\n\tOpção: '))

    if op == 1:
        print('\n\t\t\t -- Soma --\n')
    elif op == 2:
        print('\n Forte abraço!\n')
        break
    else:
        print('Opção {} incorreta!'.format(op))