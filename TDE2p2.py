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
