for numero in range(1,10):
    if numero == 5:
        break
    print("Com break:", numero)

for numero in range(1,10):
        if numero % 2 == 0:
            continue
        print("Com continue:", numero)