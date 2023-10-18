print('-=-'*25)
s1 = float(input('Digite o cumprimento do primeiro segmento: '))
s2 = float(input('Digite o cumprimento do segundo segmento: '))
s3 = float(input('Digite o cumprimento do terceiro segmento: '))
print('-=-'*25)

if (s1 + s2) > s3 and (s2 + s3) > s1 and (s3 + s1) > s2:
    print('Os três segmentos formam um triângulo')
else:
    print('Os segmentos não formam um triângulo')
