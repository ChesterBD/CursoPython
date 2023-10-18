# palavras = ['aprender', 'python', 'curso', 'video', 'preparar', 'mercado', 'trabalho',
#             'futuro']
# print(sorted(palavras))
# palavras.pop()
# print(palavras)
# palavras.append('Chester')
# print(palavras)
# palavras.remove('Chester')
# print(palavras)
# palavras.insert(1, 'Chester')
# print(palavras)
# del palavras[1]
# print(palavras)
# palavras[-1] = 'Portugal'
# print(palavras)
# palavras.sort(reverse=True)
# print(palavras)
valores = []
for c in range(0, 5):
    valores.append(int(input('Entre com um número: ')))
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print(f'O menor número é o {min(valores)} e o maior número é {max(valores)}')
copia_valores = valores.copy()
print(copia_valores)
valores[2] = 9
print(valores)
