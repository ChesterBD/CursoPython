print('\033[45m    CALCULE SEU IMC    \033[m')
peso = float(input('Entre com o seu peso: '))
altura = float(input('Entre com sua altua: '))
imc = peso/altura**2
if imc <= 18.5:
    print("""Seu IMC é: {:.2f}
\033[43m  ABAIXO DO NORMAL!  \033[m
Procure um médico. 
Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. 
Outras podem estar enfrentando problemas, como a desnutrição. 
É preciso saber qual é o caso.""".format(imc))
elif 18.6 <= imc <= 24.9:
    print("""Seu IMC é: {:.2f}
\033[42m  NORMAL  \033[m
Que bom que você está com o peso normal! 
E o melhor jeito de continuar assim é 
mantendo um estilo de vida ativo e uma alimentação equilibrada.""".format(imc))
elif 25.0 <= imc <= 29.9:
    print("""Seu IMC é: {:.2f}
\033[45m  SOREPESO  \033[m
Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa 
já apresentam doenças associadas, como diabetes e hipertensão. 
Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, 
entrar na faixa da obesidade pra valer.""".format(imc))
elif 30.0 <= imc <= 34.9:
    print("""Seu IMC é: {:.2f}
\033[41m  OBESIDADE GRAU I  \033[m
Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. 
Vamos dar início a mudanças hoje! Cuide de sua alimentação. 
Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.""".format(imc))
elif 35.0 <= imc <= 39.9:
    print("""Seu IMC é: {:.2f}
\033[41m  OBESIDADE GRAU II  \033[m
Mesmo que seus exames aparentem estar normais, é hora de se cuidar, 
iniciando mudanças no estilo de vida com o acompanhamento próximo de 
profissionais de saúde.""".format(imc))
elif imc >= 40:
    print("""Seu IMC é: {:.2f}
\033[41m  OBESIDADE GRAU III  \033[m
Aqui o sinal é vermelho, com forte probabilidade de já existirem 
doenças muito graves associadas. O tratamento deve ser ainda mais urgente.""".format(imc))
