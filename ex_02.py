import os
os.system("cls")
print("Programa que recebe o número do código e retorna o cargo correspondente")

print("""\nCódigo \tCargo
1 \tEscrituário
2 \tSecretária
3 \tCaixa
4 \tGerente
5 \tDiretor""")

codigo = int(input("\nDigite o numero do código (de 1 a 5): "))

if codigo<1 or codigo>5:
    print("Número invalido")
else:
    if codigo == 1:
        print(f"\t{codigo} - Escrituário")
    elif codigo == 2:
        print(f"\t{codigo} - Secretária")
    elif codigo == 3:
        print(f"\t{codigo} - Caixa")
    elif codigo == 4:
        print(f"\t{codigo} - Gerente")
    else:
        print(f"\t{codigo} - Diretor")