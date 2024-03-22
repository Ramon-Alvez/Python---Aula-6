import os
os.system("cls")

print("Programa que calcula a conta final do Hotel")

print("\nBem vindo ao Hotel Capybara.py")

nome = str(input("\nPor favor, digite o nome do cliente: "))
apartamento = str(input("Digite o tipo do apartamento escolhido pelo cliente (A a D): ")).upper()
if apartamento != "A" and apartamento != "B" and apartamento != "C" and apartamento != "D":
    print("Apartamento inválido")
else:
    qtd_dias = int(input("Digite a quantidade de dias em que ficou hospedado: "))
    if qtd_dias <= 0:
        print("Quantidade inválida")
    else:
        consumo_interno = float(input("Digite o valor gasto pelo consumo interno do cliente: "))
        if consumo_interno < 0:
            print("Valor inválido")
        else:
            if apartamento == "A":
                diaria = 150
                total_diaria = qtd_dias * diaria
            elif apartamento == "B":
                diaria = 100
                total_diaria = qtd_dias * diaria
            elif apartamento == "C":
                diaria = 75
                total_diaria = qtd_dias * diaria
            else:
                diaria = 50
                total_diaria = qtd_dias * diaria
            total = total_diaria + consumo_interno
        print(f"""\nConta do hotel Capybara.py
\nCliente: {nome};
Apartamento tipo: {apartamento} \tValor da diária: R$ {diaria:.2f}
Dias hospedados: {qtd_dias:.0f} \tValor total das diárias: R$ {total_diaria:.2f}
Consumo interno total: R$ {consumo_interno:.2f}

Total: R$ {total:.2f}

Obrigado por se hospedar conosco!
Volte sempre!! :D""")
