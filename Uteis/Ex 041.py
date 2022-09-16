#indice de massa corporal

peso = float(input('Digite seu peso: ').strip())
altura = float(input('Digite sua altura: ').strip())

imc = peso/ (altura ** 2)
print("Seu IMC equivale à: {:.1f}".format(imc))

if (imc < 18.5):
    print("Abaixo do ideal.")
elif (imc >= 18.5 and imc < 25):
    print("Indíce ideal.")
elif (imc >= 25 and imc < 30):
    print("Sobre-peso")
elif (imc >= 30):
    print("Obesidade, procure um médico.")