dias = int(input("Digite a quantidade de dias:  \n"))
km = float(input("Digite quantos KM rodou: \n"))
custo_dias = (dias * 60)
custo_km = (km * 0.15)
print("Você andou {}KM por {} dias, então o preço a pagar é R${:.2f}".format(km, dias, (custo_km + custo_dias)))
