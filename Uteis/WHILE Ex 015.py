#CAIXA ELETRONICO

print("=="*20)
print("{:^37}".format("BANCO DO MANCO"))
print("=="*20)


valor = int(input('Qual valor você quer sacar? R$ ').strip())
total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"Total de {total_ced} cédula de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

print("=="*20)
print("VOLTE SEMPRE AO BANCO DO MANCO")