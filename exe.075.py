par = 0
n1 = int(input('Entre com o 1º número: '))
if n1 % 2 == 0:
    par += 1
n2 = int(input('Entre com o 2º número: '))
if n2 % 2 == 0:
    par += 1
n3 = int(input('Entre com o 3º número: '))
if n3 % 2 == 0:
    par += 1
n4 = int(input('Entre com o 4º número: '))
if n4 % 2 == 0:
    par += 1
n5 = int(input('Entre com o 5º número: '))
if n5 % 2 == 0:
    par += 1

tupla = (n1, n2, n3, n4, n5)
print(f'Os números digitados foram: {tupla}')
print(f'A quantidade de número 9 é: {tupla.count(9)}')
print(f'O número que está na 3ª posição é: {tupla[3]}')
print(f'Nessa tupla, {par} número(s) são/é par(es)')
