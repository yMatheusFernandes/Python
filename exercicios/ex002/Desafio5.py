print("Analisando tipos primitivos de dados e exemplificando a verificação de caracteres em strings com python")

a = input("Digite um valor")

print(f"O valor digitado é um {a}")
print(f"O valor possui o tipo primitivo {type(a)}")

print(f"Todos os caracteres na string são letras? {a.isalpha()}")
print(f"Todos os caracteres na string são numericos?{a.isnumeric()}")
print(f"Todos os caracteres na string são digitos?{a.isdigit()}")
print(f"todos os caracteres na string são alphanumericos?{a.isalnum()}")
print(f"Todos os caracteres na string são espaços em branco?{a.isspace()}")
print(f"Todos os caracteres na string são letras maisculas?{a.isupper()}")
print(f"Todos os caracteres na string são letras minusculas?{a.islower()}")
print(f"A string estar no formato de titulo?{a.istitle()}")

"""
print(s1.isalpha())  # True
print(s2.isnumeric())  # True
print(s3.isalnum())  # True
print(s4.isspace())  # True
print(s5.isupper())  # True
print(s6.islower())  # True
print(s7.istitle())  # True
"""
