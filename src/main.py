
#PARTICIPANTES Renan Belem, Gabriel Sposito, Thomas Frentzel, Pedro Amadeu

while True:
    print('-' * 70)
    print('Digite o número da operação que deseja realizar:')
    print('1 - Conversão de base numérica\n2 - Soma / Subtração\n3 - Sair')
    print('-' * 70)
    x = int(input('>>>>> '))

    if x == 1:      #conversoes de base
        print('\n1 - Binária\n2 - Octal\n3 - Decimal\n4 - Hexadecimal')
        basei = int(input('\nDigite o valor correspondente a base inicial: '))
        print('\n1 - Binária\n2 - Octal\n3 - Decimal\n4 - Hexadecimal')
        basef = int(input('\nDigite o valor correspondente a base que o número será convertido:\n '))
        if basei == basef:
            print('Escolha duas bases diferentes para conversão! Tente novamente.')
            exit()

        if basei == 1:      #conversoes de binario para outras
            n = input('Digite o número inteiro em binário que deseja converter: ')
            ndec = int(n, 2)
            if basef == 2:
                if ndec >= 0:
                    print('O valor "{}" de base binária, convertido para base octal é: "{}"'.format(n, oct(ndec)[2:]))
                else:
                    print('O valor "{}" de base binária, convertido para base octal é: "-{}"'.format(n, oct(ndec)[3:]))
            if basef == 3:
                if ndec >= 0:
                    print('O valor "{}" de base binária, convertido para base decimal é: "{}"'.format(n, ndec))
                else:
                    print('O valor "{}" de base binária, convertido para base decimal é: "-{}"'.format(n, ndec))
            if basef == 4:
                if ndec >= 0:
                    print('O valor "{}" de base binária, convertido para base hexadecimal é: "{}"'.format(n, hex(ndec)[2:]))
                else:
                    print('O valor "{}" de base binária, convertido para base hexadecimal é: "-{}"'.format(n, hex(ndec)[3:]))

        elif basei == 2:       #conversoes de octal para outras
            n = input('Digite o número inteiro em octal que deseja converter: ')
            ndec = int(n, 8)
            if basef == 1:
                if ndec >= 0:
                    print('O valor "{}" de base octal, convertido para base binária é: "{}"'.format(n, bin(ndec)[2:]))
                else:
                    print('O valor "{}" de base octal, convertido para base binária é: "-{}"'.format(n, bin(ndec)[3:]))
            if basef == 3:
                if ndec >= 0:
                    print('O valor "{}" de base octal, convertido para base decimal é: "{}"'.format(n, ndec))
                else:
                    print('O valor "{}" de base octal, convertido para base decimal é: "-{}"'.format(n, ndec))
            if basef == 4:
                if ndec >= 0:
                    print('O valor "{}" de base octal, convertido para base hexadecimal é: "{}"'.format(n, hex(ndec)[2:]))
                else:
                    print('O valor "{}" de base octal, convertido para base hexadecimal é: "-{}"'.format(n, hex(ndec)[3:]))

        elif basei == 3:        #conversoes de decimal para outras
            n = int(input('Digite o número inteiro em decimal que deseja converter: '))
            if basef == 1:
                if n >= 0:
                    print('O valor "{}" de base decimal, convertido para base binária é: "{}"'.format(n, bin(n)[2:]))
                else:
                    print('O valor "{}" de base decimal, convertido para base binária é: "-{}"'.format(n, bin(n)[3:]))
            if basef == 2:
                if n >= 0:
                    print('O valor "{}" de base decimal, convertido para base octal é: "{}"'.format(n, oct(n)[2:]))
                else:
                    print('O valor "{}" de base decimal, convertido para base octal é: "-{}"'.format(n, oct(n)[3:]))
            if basef == 4:
                if n >= 0:
                    print('O valor "{}" de base decimal, convertido para base hexadecimal é: "{}"'.format(n, hex(n)[2:]))
                else:
                    print('O valor "{}" de base decimal, convertido para base hexadecimal é: "-{}"'.format(n, hex(n)[3:]))

        elif basei == 4:        #conversoes de hexadecimal para outras
            n = input('Digite o número inteiro em hexadecimal que deseja converter: ')
            ndec = int(n, 16)
            if basef == 1:
                if ndec >= 0:
                    print('O valor "{}" de base hexadecimal, convertido para base binária é: "{}"'.format(n, bin(ndec)[2:]))
                else:
                    print('O valor "{}" de base hexadecimal, convertido para base binária é: "-{}"'.format(n, bin(ndec)[3:]))
            if basef == 2:
                if ndec >= 0:
                    print('O valor "{}" de base hexadecimal, convertido para base octal é: "{}"'.format(n, oct(ndec)[2:]))
                else:
                    print('O valor "{}" de base hexadecimal, convertido para base octal é: "-{}"'.format(n, oct(ndec)[3:]))
            if basef == 3:
                if ndec >= 0:
                    print('O valor "{}" de base hexadecimal, convertido para base decimal é: "{}"'.format(n, ndec))
                else:
                    print('O valor "{}" de base hexadecimal, convertido para base decimal é: "-{}"'.format(n, ndec))

        else:
            print('Digite um número válido! Tente novamente.')
            exit()

    elif x == 2:        #soma e subtraçao
        print('Você deseja somar ou subtrair os dois valores?')  # soma ou subtraçao
        opcao = int(input('1 - Somar\n2 - Subtrair\n>>>>>> '))
        print('\n1 - Binária\n2 - Octal\n3 - Decimal\n4 - Hexadecimal')
        base1 = int(input('\nDigite o valor correspondente a base do primeiro número da operação: '))
        if base1 == 1:
            n = input('Digite o primeiro número inteiro da operação em binário: ')
            ndec = int(n, 2)

        if base1 == 2:
            n = input('Digite o primeiro número inteiro da operação em octal: ')
            ndec = int(n, 8)

        if base1 == 3:
            n = int(input('Digite o primeiro número inteiro da operação em decimal: '))
            ndec = n

        if base1 == 4:
            n = input('Digite o primeiro número inteiro da operação em hexadecimal: ')
            ndec = int(n, 16)

        print('\n1 - Binária\n2 - Octal\n3 - Decimal\n4 - Hexadecimal')
        base2 = int(input('\nDigite o valor correspondente a base do segundo número da operação: '))
        if base2 == 1:
            n2 = input('Digite o segundo número inteiro da operação em binário: ')
            ndec2 = int(n2, 2)

        if base2 == 2:
            n2 = input('Digite o segundo número inteiro da operação em octal: ')
            ndec2 = int(n2, 8)

        if base2 == 3:
            n2 = int(input('Digite o segundo número inteiro da operação em decimal: '))
            ndec2 = n2

        if base2 == 4:
            n2 = input('Digite o segundo número inteiro da operação em hexadecimal: ')
            ndec2 = int(n2, 16)

        if opcao == 1:
            resultado = ndec + ndec2
        elif opcao == 2:
            resultado = ndec - ndec2
        else:
            print('Escolha uma opção válida! Tente novamente.')
            exit()

        if resultado>=0:
            print('\nO resultado da soma dos valores nas diferentes bases númericas é:')
            print(f'Binário: {bin(resultado)[2:]}')
            print(f'Octal: {oct(resultado)[2:]}')
            print(f'Decimal: {resultado}')
            print(f'Hexadecimal: {hex(resultado)[2:]}')
        else:
            print('\nO resultado da soma dos valores nas diferentes bases númericas é:')
            print(f'Binário: -{bin(resultado)[3:]}')
            print(f'Octal: -{oct(resultado)[3:]}')
            print(f'Decimal: {resultado}')
            print(f'Hexadecimal: -{hex(resultado)[3:]}')

    elif x == 3:        #sair
        print("Até a próxima!")
        exit()
    else:               #escolha fora das possiveis
        print('Por favor digite um número válido!')