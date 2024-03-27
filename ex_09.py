import os
os.system("cls")

print("Cálculo do grau de obesidade de uma pessoa")

peso = float(input("\nDigite o seu peso: "))
altura = float(input("Digite a sua altura: "))

if peso < 0 or altura < 0:
    print("Valores inválidos")
else:
    massa = peso / (altura**2)
    if massa < 26:
        print("O seu grau é considerado como: normal")
    elif massa >= 26 and massa < 30:
        print("O seu grau é considerado como: obeso")
    else:
        print("O seu grau é considerado como: Obeso mórbido.")