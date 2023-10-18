print('\033[42mConversão de Base\033[m')
num = int(input('Digite um número inteiro para a conversão: '))
print("""Escolha uma base para a coversão:
[1] Binário
[2] Octal
[3] Hexadecimal""")
op = int(input("Sua opção: "))
if op == 1:
    print('O número {} em Binário é: {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('O número {} em Octal é: {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('O número {} em Hexadecimal é: {}'.format(num, hex(num)[2:]))
