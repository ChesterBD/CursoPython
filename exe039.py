import datetime
hj = int(datetime.datetime.now())
print('-=-' * 12)
print('\033[42m   Alistamento Militar Origatório \033[m')
print('-=-' * 12)
print("""Qual é o seu Sexo?
[1] Masculino
[2] Feminino""")
sexo = int(input('Digite sua opção: '))
if sexo == 2:
    print('Você não precisa se Alistar!!!')
elif sexo == 1:
    nasc = int(input('Digite o ano do seu nascimento: '))
    idade = int(hj.year - nasc)
    aa = nasc + 17
if idade == 17:
    print('\033[42m Parabéns! \033[m Esse é o ano do seu Alistamento Militar! Você está com {} anos.'.format(idade))
elif idade < 17:
    print('Seu Alistamento é daqui a {} ano(s)'.format(17 - idade))
elif 18 <= idade < 21:
    print("""\033[41mVocê deve se Alistar Imediatamente!!!\033[m 
        Você deveria ter se alistado em {}. Procure um posto mais próximo!""".format(aa))
elif idade > 21:
    print('Você tem {} anos! Espero que esteja quite com suas Obrigações Miliares!'.format(idade))
