times = ('Botafogo', 'Flamengo', 'Athletico-PR', 'Bahia', 'Palmeiras',
         'São Paulo', 'Bragantino', 'Cruzeiro', 'Atlético-MF', 'Juventude', 'Fortaleza', 'Internacional', 'Cuiabá', 'Criciuma', 'Atlético-Go', 'Vasco da Gama', 'Corinthians',
         'Fluminence', 'Grêmio', 'EC Vitória')
print('*=*'*50)
print(f'Os 5 primeiros times são {times[:5]}')
print('*=*'*50)
print(f'Os 5 ultimos são {times[-5:]}')
print('*=*'*50)
print(f'Os times em ordem alfabetica são {sorted(times)}')
print('*=*'*50)
print(f'Fortaleza está na posição {times.index('Fortaleza')+1}')