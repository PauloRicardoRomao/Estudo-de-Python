#verifica se emprestimo é aceito ou não

valor_casa = float(input('Insira o valor da casa: R$'))
salario = float(input('Insira aqui seu salário: R$'))
tempo_pagam = int(input('Insira em quanto tempo deseja pagar(em anos): '))

parcela_mensal = valor_casa/(tempo_pagam *12)


print('Valor da casa R${:.2f}'.format(valor_casa))
#print('Salário R${:.2f}'.format(salario))
#print('Anos de prestação {}'.format(tempo_pagam))
print('Valor de cada parcela corresponde à R${:.2f}'.format(parcela_mensal))
porcentagem = salario*(30/100)
#print('30% do seu salário equivale à {}'.format(porcentagem))
if (parcela_mensal <= porcentagem):
    print("EMPRÉSTIMO ACEITO.")
elif (parcela_mensal > porcentagem):
    print("EMPRÉSTIMO NEGADO, às parcelas excedem 30% do seu salário, acima do permitido.")
else:
    print("Insira um valor válido.")