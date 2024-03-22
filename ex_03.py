import os
os.system("cls")

print("""Programa que recebe uma idade e determina se essa pessoa é considerado
       eleitor obrigatório, faculdativo ou não eleitor.""")

idade = int(input("\nDigite a idade que deseja conferir: "))

if idade < 0 or idade >150:
    print("Idade invalida")
else:
    if idade < 16:
        print("Não eleitor")
    elif idade >= 18 and idade <= 65:
        print("Eleitor obrigatório")
    else:
        print("Eleitor facultativo")