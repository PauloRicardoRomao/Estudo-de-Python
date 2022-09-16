#ANALISADOR DE IDADE
import datetime
atual = datetime.date.today().year
contmaior = 0
contmenor = 0

#datanasc = int(input('Digite o ano de nascimento: ').strip())

for c in range(1, 4+1):
    print("-="*18)
    datanasc = int(input('Digite o ano de nascimento: ').strip())

    if atual < datanasc:
        print("Insira um ano válido.")
    else:
        idade = atual-datanasc
        print("Sua idade é {} anos.".format(idade))
        if idade >= 18:
            print("Você é MAIOR de idade.")
            contmaior += 1
        else:
            print("Você é MENOR de idade.")
            contmenor += 1
print("-="*18)
print("\n\33[33mAo todo são {} MAIORES de idade".format(contmaior))
print("\33[33mAo todo são {} MENORES de idade".format(contmenor))
