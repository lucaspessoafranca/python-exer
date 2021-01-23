t_carros ("HRV", "GOLF", "ARGO")
# Tuplas são imutáveis.
l_carros=list(t_carros) # lista carros recebe os valores da tupla
l_carros[2] =' FOCus '
t_carros=tuple(l_carros)

for x in t_carros:
    print(x)