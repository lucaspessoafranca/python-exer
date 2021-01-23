carros = [['Modelo',"HRV"],
          ["Fabricante",'Honda'],
          ['Ano', "2016"]]
print(carros[0][0])
print(carros[0][1])
carros.append(['Cor', 'Prata'])
for l,c in carros:
    print(f'Linha: {l}, Coluna: {c}\n')