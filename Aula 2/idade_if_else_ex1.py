idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Você é criança")
elif idade <= 17:
    print("Você é adolescente")
elif idade <= 64:
    print("Você é adulto")
else:
    print("Você é idoso")