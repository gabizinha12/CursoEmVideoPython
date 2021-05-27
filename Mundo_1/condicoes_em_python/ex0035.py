r1 = float(input("Digite o comprimento da segunda reta:  "))
r2 = float(input("Digite o comprimento da segunda reta:   "))
r3 = float(input("Digite o comprimento da terceira reta:  "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r2:
    print("Com as retas acima é possível fazer um triângulo")
else:
    print("Não é possível formar um triângulo")
