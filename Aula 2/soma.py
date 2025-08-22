n = int(input("Digite um número: "))

soma=0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma += i
        print(f"A soma dos números pares de 1 a {n} é: {soma}")