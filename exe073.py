clube = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fortaleza',
         'Fluminense', 'Atlético-PR', 'Atlético-MG', 'São Paulo', 'Cuiabá', 'Internacional',
         'Corinthians', 'Santos', 'Cruzeiro', 'Bahia', 'Vasco', 'Goiás', 'Coritiba', 'América-MG')
print(f'Os Top 5 são: {clube[:5]}')
print(f'Os 4 últimos colocados são: {clube[-4:]}')
print(f'Os Clubes em Ordem sao: {sorted(clube)}')
print(f"O Flamengo está na [{clube.index('Flamengo') + 1}ª] posição da tabela.")
