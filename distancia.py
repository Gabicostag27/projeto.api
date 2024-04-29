origem = input("Cidade de origem: ")
destino = input("Cidade de destino: ")
distancia = float(input("Qual a distâmcia em km? "))
velocidade = float(input("Quantos km/h irá viajar? "))
tempo = distancia/velocidade*60
nome_motorista = input("Digite o nome do motorista")
print(f"{nome_motorista} você levará {tempo} minutos de {origem} à {destino}")
