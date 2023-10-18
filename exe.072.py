print('\033[43m              TUPLAS              \033[m')
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Entre com um número de 0 à 20: '))
while num > 20:
    num = int(input('Entre com um número válido! '))
print(f'Muito bem! Você digitou o número: [{tupla[num]}]')
