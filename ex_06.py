import os
os.system("cls")

print("Cálculo da multa com base no peso excedente de peixes")

peso_total = float(input("\nDigite o peso total (kg) dos peixes pescados: "))

if peso_total < 0:
    print("Peso inválido")
else:
    if peso_total <= 50:
        excesso = 0
        multa = 0
    else:
        excesso = peso_total - 50
        multa = excesso * 4
    print(f"""\nApós pescar {peso_total:.1f}Kgs de peixe, temos:
          Excesso de {excesso:.1f}Kgs;
          E a multa de R$ {multa:.2f}.""")