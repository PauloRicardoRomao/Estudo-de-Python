# ler velocidade do carro e mostrar se tera multa ou não
vel_carro = int(input('Qual a velocidade do carro?  '))
print("A velocidade do carro é {}km".format(vel_carro))

if (vel_carro > 80):
    print("Seu carro ultrapassou o limite de velocidade, você está multado.")
    multa = (vel_carro - 80) * 7.00
    print("Sua multa equivale à R${:.2f}.".format(multa))
print("Dentro da velocidade permitida, tenha um bom dia.")

