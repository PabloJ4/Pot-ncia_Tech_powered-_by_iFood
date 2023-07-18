'''
Desafio
Você está criando um aplicativo de entrega de comida e precisa calcular o preço final do pedido do usuário. O usuário escolheu alguns itens do cardápio e é preciso calcular o preço total do pedido.
'''
valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

#TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
valor_total = (valorHamburguer*quantidadeHamburguer) + (valorBebida*quantidadeBebida)

#TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
troco = valorPago - valor_total
#TODO: Imprimir a saída no formato especificado neste desafio.

print(f"O preço final do pedido é R$ {valor_total:.2f}. Seu troco é R$ {troco:.2f}.")