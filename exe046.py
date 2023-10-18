import time
print('\033[44m   CONTAGEM REGRESSIVA   \033[m')
for c in range(5, 0, -1):
    print(c)
    time.sleep(1)
print('Fim!')
