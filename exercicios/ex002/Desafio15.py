print("              Aluguel de carros             ")

days = float(input('Por quantos dias o carro foi usado ? '))

km = float(input('Quantos km foi rodado no carro ? '))

print(f'Considerando uma taxa de R$60,00 ao dia e R$00,15 o Km rodado deu R${days*60:.2f} pelos dias e R${km*0.15:.2f} pelos km rodados')