'''
Desafio
O objetivo deste programa é ajudar a equipe do Restaurante Veggieworld a identificar rapidamente os pedidos veganos e não veganos e informar as calorias de cada prato definido pelo cliente. O programa deve solicitar ao usuário o número de pedidos que serão feitos e, em seguida, pedir informações sobre cada pedido, incluindo se o prato é vegano ou não (usando as opções "s" para sim e "n" para não) e a quantidade de calorias. Ao final, o programa deve exibir uma lista de todos os pedidos com suas informações correspondentes.
'''

import sys

def exibir_pedido(numero_pedido, nome_prato, eh_vegano, calorias):
    tipo_vegano = "Vegano" if eh_vegano else "Nao-vegano"
    print(f"Pedido {numero_pedido}: {nome_prato} ({tipo_vegano}) - {calorias} calorias")

# Obter o número de pedidos
n = int(input().strip())

pedidos = []
# Obter informações sobre cada pedido
for i in range(1, n+1):
    nome_prato = input().strip()
    calorias = int(input().strip())
    eh_vegano = input().strip().lower() == "s"
    pedidos.append((i, nome_prato, eh_vegano, calorias))

# Exibir a lista de pedidos
for pedido in pedidos:
    exibir_pedido(*pedido)