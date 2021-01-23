#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

distancia = float(input('Digite a distâcia em metros :'))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10 
cm = distancia * 100
mm = distancia * 11000

print(f'A distância de {distancia:.1f}Metros equivale a {cm:.1f}CM e {mm:.1f}MM')