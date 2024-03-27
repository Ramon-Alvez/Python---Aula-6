import os
os.system("cls")

print("Programa que calcula a declaração do imposto de renda")

nome = str(input("\nDigite o seu nome: "))
cpf = str(input("Digite seu CPF (sem formatação, ex: xxxxxxxxxxx): "))
renda_anual = int(input("Digite sua renda anual: R$ "))
qtd_dependentes = int(input("Digite o número de dependentes: "))

#  Seleção de dados inválidos
if renda_anual < 0 or qtd_dependentes < 0:
    print("Valores inválidos")
else:
    renda_liquida = renda_anual/12

#  Seleção de alíquota comparando o salário líquido com base tabelada do Imposto de Renda

    if renda_liquida <= 800:
        aliquota = 0
    elif renda_liquida > 800 and renda_liquida <= 4000:
        aliquota = 2.5
    elif renda_liquida > 400 and renda_liquida <= 9000:
        aliquota = 5
    else:
        aliquota = 10

#  Cálculos príncipais
    contribuicao = renda_liquida * (aliquota/100)
    desconto_dependentes = qtd_dependentes * 110
    imposto_renda = contribuicao - desconto_dependentes

#  Condição de Isenção do Imposto de Renda
    if imposto_renda <= 0:
        print(f"""\nNome do colaborador: {nome}
CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}
Renda anual: R${renda_anual} \tRenda líquida: R${renda_liquida}

O senhor está isento de pagar o Imposto de Renda.""")

    else:
        print(f"""\nNome do colaborador: {nome}
CPF: {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}
Renda anual: R${renda_anual} \tRenda líquida: R${renda_liquida}
Qtd. de Dependentes: {qtd_dependentes} \tDesconto por dependentes: R${desconto_dependentes}
Aliquota de desconto: {aliquota}%

O valor a ser pago no imposto de renda é de: R$ {imposto_renda:.2f}.""")