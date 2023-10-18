print('\033[42;52m     PALÍNDROMO     \033[m')
frase = str(input('Digite uma frase: ').strip().upper())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
    print('\033[42m Essa frase é um Palíndromo! \033[m')
else:
    print('\033[41m Essa frase não é um Palíndromo! \033[m')
