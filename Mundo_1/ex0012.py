preco = float(input("Digite o preço do produto: \nR$"))
desconto = preco * 5 / 100
print("Na liquidação da loja, esse produto de R${:.2f} está com desconto de 5%, \n ou seja,  vai custar só R${:.2f}"
      .format(preco, preco - desconto))

