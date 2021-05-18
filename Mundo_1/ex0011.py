largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura:  "))
area = largura * altura
print("Sua parede tem dimensão {}x{} e sua área é de {}m².".format(largura, altura, area))
tinta_necessaria = area / 2
print("Para pintar essa parede vc vai precisar de {}L de tinta".format(tinta_necessaria))
