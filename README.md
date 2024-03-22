# Python---Aula-6
Exercícios básicos sobre condicional (if, else e elif) em Python, realizados durante a aula de Software básico - UMC

Lista de Exercícios:

1- Criar um algoritmo receba a média de um aluno e mostre a situação do aluno:
  a. Aprovado -> média maior ou igual a 5;
  b. Exame -> média entre 3 e 5;
  c. Reprovado -> média menor do que 3.

2- Criar um algoritmo que receba o código correspondente ao cargo de um funcionário e mostre o cargo.
  Código | Cargo
  1        Escrituário
  2        Secretária
  3        Caixa
  4        Gerente
  5        Diretor

3- Criar um algoritmo que leia a idade de uma pessoa e informar a sua classe eleitoral:
  a. Não-eleitor (abaixo de 16 anos);
  b. Eleitor obrigatório (entre 18 e 65 anos);
  c. Eleitor facultativo (entre 16 e 18 e maior de 65 anos).

4- Criar um algoritmo que mostre o menu de opções a seguir, receba a opção do usuário e os dados necessário para executar cada operação.
  Menu de opções:
  1. Somar dois números;
  2. Multiplicar dois números;
  3. Subtrair dois números;
  4. Dividir dois números.

5- Faça um algoritmo para calcular a conta final de um hóspede de um hotel fictício, contendo: o nome do hóspede, o tipo do apartamento, o número de diárias utilizadas, o valor unitário da diária, o valor total das diárias, o valor do consumo interno, o subtotal, o valor da taxa de serviço e o total gera. Considere que:
  a. Serão lidos o nome do hóspede, o tipo do apartamento utilizado (A, B, C ou D), o número de diárias utilizadas pelo hóspede e o valor do consumo interno do hóspede;
  b. O valor da diária é determinado pela seguinte tabela:
    TIPO DO APTO.  VALOR DA DIÁRIA (R$)
    A              150,00
    B              100,00
    C               75,00
    D               50,00
  OBS: O valor total das diárias é calculado pela multiplicação do número de diárias utilizadas pelo valor da diária;
  c. O subtotal é calculado pela soma do valor total das diárias e o valor do consumo interno;
  d. O valor da taxa de serviço equivale a 10% do subtotal;
  e. O total geral resulta da soma do subtotal com a taxa de serviço

6- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável P (peso de peixes) e verifique se há excesso. Se houver, gravar na vaiável E (Excesso) e na variável M o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO.

7- Construa um algoritmo que leia 3 valores inteiros e positivos e:
  a. Encontre o maior valor;
  b. Encontre o menor valor;
  c. Calcule a média dos números lidos.

8. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
  a. Para homens: (72.7*h) - 58;
  b. Para mulheres: (62.1*h) - 44.7;
  Obs: h = altura

9. Escreva um algoritmo que determine o grau de obesidade de uma pessoa, sendo fornecido o peso e a altura da pessoa. O grau de obesidade é determinado pelo índice da massa corpórea (Massa = Peso / Altura²) através da tabela abaixo:
   MASSA CORPÓREA  GRAU DE OBESIDADE
       < 26        Normal
   >= 26 e < 30    Obeso
       >= 26       Obeso mórbido

10. Na declaração de imposto de renda devem constar os dados: nome do contribuinte, CPF, renda anual e número de dependentes. Os cálculos são feitos da forma a seguir:
    a. Desconto de R$ 110,00 por dependente
    b. Com base na renda líquida (renda anual menos descontos) é calculada a alíquota de contribuição de acordo com a tabela:
    RENDA LÍQUIDA                    ALÍQUOTA (%)
    Até R$ 800,00                     Isento
    De R$ 801,00 até 4.000,00         2.5      
    De R$ 4.001,00 até R$ 9.000,00    5
    Acima de R$ 9.000,00              10
Elabore o programa para calcular o valor do imposto (Renda líquida * Alíquota) a ser pago por um contribuinte.
