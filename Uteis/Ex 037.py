#converte o numero escolhido
numero = int(input('Insira um número: '))

print('''Escolha a base da conversão...
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal''')

base = input('Insira como deseja ser convertido: ').strip()

if (base == '1'):
    print('Você escolheu binário, o número {} na forma de binário é...'.format(numero))
    print(bin(numero))
elif (base == '2'):
    print('Você escolheu octal, o número {} na forma de octal é...'.format(numero))
    print(oct(numero))
elif (base == '3'):
    print('Você escolheu hexadecimal, o número {} na forma de hexadecimal é...'.format(numero))
    print(hex(numero))