import os
os.system("cls")

print("""Programa que compara 3 valores inteiros positivos e:
      a. Separa o maior número;
      b. Separa o menor número;
      c. Cálcula a média entre os 3 valores.""")
n1 = int(input("\nDigite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 < 0 or n2 < 0 or n3 < 0:
    print("Valores inválidos")
else:
    if n1 > n2 and n1 > n3:
        maior = n1
    elif n2 > n1 and n2 > n3:
        maior = n2
    else:
        maior = n3
    
    if n1 < n2 and n1 < n3:
        menor = n1
    elif n2 < n1 and n2 < n3:
        menor = n2
    else:
        menor = n3
    media = (n1 + n2 + n3)/3
    print(f"""\nPara os valores {n1}, {n2} e {n3}, temos:
          a. O maior número: {maior};
          b. O menor número: {menor};
          c. A média entre os 3 números: {media:.1f}.""")