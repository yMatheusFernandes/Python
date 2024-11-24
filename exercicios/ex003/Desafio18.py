import math

# Solicita o ângulo ao usuário
angulo = float(input("Digite o valor de um ângulo em graus: "))

# Converte o ângulo de graus para radianos
angulo_rad = math.radians(angulo)

# Calcula o seno, cosseno e tangente
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

# Exibe os resultados
print(f"O ângulo de {angulo} graus tem:")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")