print('\033[45m    CONDIÇÃO DE EXISTÊNCIA DO TRIÂNGULO    \033[m')
s1 = int(input('Digite o cumprimento do primeiro segmento: '))
s2 = int(input('Digite o cumprimento do segundo segmento: '))
s3 = int(input('Digite o cumprimento do terceiro segmento: '))
if s1 < (s2+s3) and s2 < (s1+s3) and s3 < (s1+s2):
    if (s1 == s2 != s3) or (s1 == s3 != s2) or (s2 == s3 != s1):
        print('Os segmentos formam um triângulo ISOSCELES')
    elif s1 != s2 != s3:
        print('Os segmentos formam um triângulo ESCALENO')
    elif s1 == s2 and s2 == s3:
        print('Os segmentos formam um triângulo EQUILÁTERO')
else:
    print('Os segmentos não formam um triângulo!')
