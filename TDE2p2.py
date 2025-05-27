#1. Faça um programa que receba dois números e mostre qual deles é o maior.
print("Digite dois números diferentes.")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

if n1 > n2:
    print(f"O número {n1}, é maior que o número {n2}")
else:
    print(f"O número {n2}, é maior que é o número {n1}")

#2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
n = float(input("Digite um número para calcular sua raiz quadrada: "))

if n >= 0:
    raiz = (n**0.5)
    print(f"{raiz:.2f}")
else:
    print("Número inválido")

#3. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado
n = float(input("Digite um número real: "))
if n >= 0:
    raiz = (n**0.5)
    print(f"{raiz:.2f}")
else:
    quadrado = (n**2)
    print(f"{quadrado:.2f}")

#4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# O número digitado ao quadrado; A raiz quadrada do número digitado.
n = float(input("Digite um número: "))
if n >= 0:
    raiz = (n**0.5)
    quadrado = (n**2)
    print(f"Esse número ao quadrado é {quadrado:.2f} e raiz quadrada do número é {raiz:.2f}")
else:
    print("Número inválio")

#5. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
n = int(input("Digite um número para saber se ele é par ou ímpar: "))
if n % 2 != 0:
    print("Ímpar")
else:
    print("Par") 

#6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
print("Digite dois números inteiros para mostrar o maior deles e a diferença entre ambos.")
n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
diferenca = n1 - n2

if n1 > n2:
    print(f"O número {n1}, é maior que o número {n2}. Sendo a diferença entre eles {diferenca}")
else:
    print(f"O número {n2}, é maior que é o número {n1}. Sendo a diferença entre eles {diferenca}")

#7. Escreva um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem "números iguais".
print("Digite dois números diferentes.")
n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))

if n1 > n2:
    print(f"O número {n1}, é maior que o número {n2}")
elif n2 == n1:
    print("Números iguais")
else: 
    print(f"O número {n2}, é maior que é o número {n1}")

#8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
print("Digite 2 notas válidas (00.0 a 10.0) para imprimir a média.")
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

if n1 and n2 < 11.0:
    media = (n1 + n2)/2
    print(media)
else:
    print ("Algum dos valores está inválido.")

#9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário, imprima: "empréstimo não concedido", caso contrário imprima: "empréstimo concedido".
print("Digite seu salário a o valor da prestação do empréstimo: ")
salario = float(input("Salário: "))
prestacao = float(input("Prestação: "))
vinte_salario = salario * 0.20

if prestacao > vinte_salario:
    print ("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")

#10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
#homens: (72.7 * h) - 58/ mulheres: (62.1 * h) - 44.7
print("Digite sua altura e o seu sexo para calcular seu peso ideal.")
h = float(input("Altura: "))
sexo = input("Sexo (Masculino ou Feminino): ")

if sexo.lower() == "masculino":
    peso_idealm = (72.7 * h) - 58
    print(f"Seu peso ideal é {peso_idealm:.2f}")
elif sexo.lower() == "feminino":
    peso_idealf = (62.1 * h) - 44.7
    print(f"Seu peso ideal é {peso_idealf:.2f}")
else:
    print("Informação inválida.")

#11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8(2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
n = int(input("Digite um número inteiro maior do que zero, para imprimir a soma de todos os seus algarismos: "))

if n <= 0:
    print("Número inválido")
else:
    soma = 0
    string_n = str(n)
    for caracteres in string_n:
        soma += int(caracteres)
    print(f"A soma dos caracteres é {soma}")

#12. Ler um número inteiro. Se o numero lido for negativo, escreva a mensagem "Número inválido". Se o número for positivo, calcular o logaritmo deste número.
import math
n = int(input("Digite um número inteiro para calcular o seu logaritmo: "))

if n < 0:
    print("Número inválido")
else:
    logaritmo = math.log(n)
    print (f"{logaritmo:.2f}")

#13. Faça um algoritmo que calcule a méia ponderada das notas de 3 provas. A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ao superior a 60 pontos.