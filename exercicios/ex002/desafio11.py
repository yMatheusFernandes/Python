print("                   Calculadora da area de uma parede")

altura = int(input(f"Quantos metros de altura tem a sua parede que serar pintada ? "))
largura = int(input(f"Quantos metros de largura tem a sua parede que serar pintada ? "))

area = altura*largura

area2 = area/2

print(f"Considerando que cada litro de tinta pinte uma area de 2m² serão necessarios {area2} litros de tinta para pintar a parede")