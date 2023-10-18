a1 = int(input('Digite o primeiro termo: '))
r = int(input('Entre com a razão: '))
decimo = a1 + (10 - 1) * r
for pa in range(a1, decimo + r, r):
    print(pa, end='-> ')
print('Fim!')
