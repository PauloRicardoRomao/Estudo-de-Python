#verificar aumento salarial

salario = float(input('Insira aqui seu salário para verificação: ').strip())
print("Seu salário é: R${:.2f}".format(salario))

if (salario > 1250.00):
    aumento = salario * 10/100
    reajuste = salario + aumento
    print("Seu salário será aumentado em 10%.")
    print("Seu salário passa a ser agora: R${:.2f}".format(reajuste))
elif (salario <= 1250.00):
    aumento = salario * 15/100
    reajuste = salario + aumento
    print("Seu salário será aumentado em 15%.")
    print("Seu salário passa a ser agora: R${:.2f}".format(reajuste))
