soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        print(c, end='|')
        soma = soma + c
print(soma)
