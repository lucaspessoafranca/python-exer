 #Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.

#b) Os últimos 4 colocados.

#c) Times em ordem alfabética.

#d) Em que posição está o time da Chapecoense.
times = ('São Paulo','Atlético MG', 'Flamengo', 'Internacional', 'Grêmio',
'Palmeiras', 'Fluminense', 'Santos', 'Corinthians','Ceará', 'Atlético Paranaense','Atlético Goianiense','Bragantino','Fortaleza', 'Sport', 'Bahia', 'Vasco da Gama', 'Goiás', 'Botafogo','Coritiba')
print('-=' * 15)
print(f'Lista de times do Brasileirão {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos são {times[-4:]}')
print(f'Times em ordem alfabética : {sorted(times)}')