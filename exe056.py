print('\033[41;54m          [ANÁLISE DE DADOS]          \033[m')
somaidade = 0
maioridade = 0
nomehmaisvelho = ''
totmulher20 = 0
for pessoa in range(1, 5):
    print('============== {}ª Pessoa ============'.format(pessoa))
    nome = str(input('Entre com o nome: ').upper().strip())
    idade = int(input('Entre com a idade: '))
    sexo = str(input('Sexo [M/F]: ').upper().strip())
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridade = idade
        nomehmaisvelho = nome
    if sexo in 'Mn' and idade > maioridade:
        maioridade = idade
        nomehmaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('\033[32m>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<\033[m')
print('A Média de idade do grupo é {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomehmaisvelho))
print('Ao todo, são {} mulher(es) com menos de 20 anos.'.format(totmulher20))
print('\033[32m>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<\033[m')
