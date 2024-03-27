import os
os.system("cls")

print("Cálculo do peso ideal com base na alura e o sexo.")

altura = float(input("\nDigite a sua altura: "))
sexo = str(input("Digite o seu Sexo (M/F): ")).upper()

if altura < 0 or sexo != "M" and sexo != "F":
    print("Valores inseridos inválidos")
else:
    if sexo == "M":
        sexo = "Masculino"
        peso_ideal = (72.7 * altura) - 58
    else:
        sexo = "Feminino"
        peso_ideal = (62.1 * altura) - 44.7
    print(f"\nCom base na altura de {altura:.2f} sendo do sexo {sexo}, o peso ideal é {peso_ideal:.1f}.")        