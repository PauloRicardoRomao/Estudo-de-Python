#pedra, papel, tesoura

from random import randint
from time import sleep

itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)

from random import randint

print("""Suas opções são:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
""")

jogador = int(input('Qual sua escolha? ').strip())
print("=-="*20)
sleep(1)
print(f"""JO
KEN
PO!!!""")
print("-="*12)
sleep(1)
print(f"O computador escolheu {itens[computador]}.")
print(f"Você escolheu {itens[jogador]}.")
print("=-="*20)
print("O VENCEDOR É...")
sleep(1)

#VENCEDOR COMPUTADOR
if jogador == 0 and computador == 1:
    print("COMPUTADOR!!!")
elif jogador == 1 and computador == 2:
    print("COMPUTADOR!!!")
elif jogador == 2 and computador == 0:
    print("COMPUTADOR!!!")
#VENCEDOR JOGADOR
if jogador == 0 and computador == 2:
    print("JOGADOR!!!")
elif jogador == 1 and computador == 0:
    print("JOGADOR!!!")
elif jogador == 2 and computador == 1:
    print("JOGADOR!!!")

else:
    print("EMPATE!!!")