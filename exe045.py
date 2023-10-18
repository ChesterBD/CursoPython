import random
import time
print('\033[43m          JOKENPO          \033[m')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.choice(lista)
minhaescolha = int(input("""FAÇA SUA ESCOLHA:
[1] PEDRA [2] PAPEL [3] TESOURA
Opção >>> """))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO')
time.sleep(1)
print('Sua escolha foi: {}'.format(lista[minhaescolha - 1]))
print('A escolha do computador foi: {}'.format(computador))
if ((computador == lista[0] and minhaescolha == 1) or
        (computador == lista[1] and minhaescolha == 2) or
        (computador == lista[2] and minhaescolha == 3)):
    print('\033[43m Empate!!! \033[m')
elif computador == lista[0] and minhaescolha == 2:
    print('\033[42m Você Ganhou!!! \033[m')
elif computador == lista[0] and minhaescolha == 3:
    print('\033[41m Você Perdeu!!! \033[m')
elif computador == lista[1] and minhaescolha == 1:
    print('\033[41m Você Perdeu!!! \033[m')
elif computador == lista[1] and minhaescolha == 3:
    print('\033[42m Você Ganhou!!! \033[m')
elif computador == lista[2] and minhaescolha == 1:
    print('\033[42m Você Ganhou!!! \033[m')
elif computador == lista[2] and minhaescolha == 2:
    print('\033[41m Você Perdeu!!! \033[m')
