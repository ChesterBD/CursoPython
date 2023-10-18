print('\033[42m      VALIDAÇÃO DO TIPO DE SEXO      \033[m')
sexo = str(input('Digite seu sexo [M/F]: ').upper().strip())
while (sexo != 'M') and (sexo != 'F'):
    valido = str(input('Por favor! Entre com uma opção Válida: ').upper().strip())
    sexo = valido
print('Você digitou [\033[32m{}\033[m]. Obrigado por digitar uma opção válida!'.format(sexo))
