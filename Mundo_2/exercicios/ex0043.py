peso = float(input("Digite seu peso:  kg"))
altura = float(input("Digite sua altura:  cm"))
imc = peso / (altura * altura)
print(f"Seu IMC é de {imc:.1f}")
if imc <= 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 25.0:
    print("Peso ideal")
elif 25.0 <= imc < 30.0:
    print("Sobrepeso")
elif 30.0 <= imc < 40.0:
    print("Obesidade")
else:
    print("Obesidade mórbida")

