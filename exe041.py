import datetime
print('\033[44m   CAMPEONATO DE NATAÇÃO   \033[m')
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
nascimento = int(input('Digite o ano do seu nasscimento: '))
idade = ano_atual - nascimento
if idade <= 9:
    print('Você tem {} anos e competirá na modalidade Mirim'.format(idade))
elif 10 <= idade <= 15:
    print('Você tem {} anos e competirá na modalidade Infantil'.format(idade))
elif 16 <= idade <= 20:
    print('Você tem {} anos e competirá na modalidade Junior'.format(idade))
elif 21 <= idade <= 30:
    print('Você tem {} anos e competirá na modalidade Senior'.format(idade))
else:
    print('Você tem {} anos e competirá na modalidade Master'.format(idade))
