import os
os.system("cls")

print("Programa que mostra a situação de um aluno baseado em sua média.")

media = float(input("\nDigite o valor da média: "))

if media < 0 or media > 10:
    print("Média inválida")
elif media >= 5:
    print("Aluno aprovado")
elif media >= 3 and media < 5:
    print("Aluno de exame")
else:
    print("Aluno reprovado")