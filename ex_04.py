import os
os.system("cls")

print("Calculadora básica")

print("""\nMenu de opções:
    1. \tSomar dois numeros;
    2. \tMultiplicar dois numeros;
    3. \tSubtrair dois numeros;
    4. \tDividir dois numeros.""")

menu = int(input("\nDigite o numero que representa a opção desejada: "))
if menu < 1 or menu > 4:
    print("Numero inválido")
else:
    num_1 = float(input("\nDigite o primeiro número: "))
    num_2 = float(input("Digite o segundo número: "))
    if menu == 1:
        resultado = num_1 + num_2
        print(f"\nO resultado da operação {num_1:.2f} + {num_2:.2f} é igual a {resultado:.2f}.")
    elif menu == 2:
        resultado = num_1 * num_2
        print(f"\nO resultado da operação {num_1:.2f} x {num_2:.2f} é igual a {resultado:.2f}.")
    elif menu == 3:
        resultado = num_1 - num_2
        print(f"\nO resultado da operação {num_1:.2f} - {num_2:.2f} é igual a {resultado:.2f}.") 
    elif num_2 == 0:
        print("\nNão é possível divisão por 0.")
    else: 
        resultado = num_1 / num_2
        print(f"\nO resultado da operação {num_1:.2f} / {num_2:.2f} é igual a {resultado:.2f}.") 