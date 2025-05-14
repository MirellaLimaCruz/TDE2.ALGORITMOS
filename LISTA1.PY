#1. Faça um programa que leia um numero inteiro e o imprima.
numero_inteiro = int(input("Digite um número inteiro: "))
print(numero_inteiro)

#2. Faça um programa que leia um numero real e o imprima.
numero_real = float(input("Digite um número real: "))
print(numero_real)

#3. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))
valor3 = int(input("Digite mais outro número: "))
soma = valor1 + valor2 + valor3
print("A soma dos três valores é:", soma)

#4. Leia um numero real e imprima o resultado do quadrado desse número.
n_real = float(input("Digite um número real: "))
quadrado_n = n_real**2
print("Aqui o quadrado desse número:", quadrado_n)

#5. Leia um numero real e imprima a quinta parte deste número.
num_real = float(input("Digite um número: "))
quinta_parte = round(num_real/5, 2)
print("A quinta parte desse número é: ", quinta_parte)

#6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A formula de conversão é: F = C∗(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
C = float(input("Digite uma temperatura em Celsius: "))
F = round(C * (9.0/5.0) + 32.0, 2)
print("A temperatura, agora em Fahrenheit: ", F)

#7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A formula de conversão é: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
F = float(input("Digite uma temperatura em Fahrenheit: "))
C = round(5.0 * (F - 32.0)/9.0, 2)
print("A temperatura, agora em Celsius: ", C)

#8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A formula de conversão é: ́C = K − 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
K = float(input("Digite uma temperatura em Kelvin: "))
C = round(K - 273.15, 2)
print ("A temperatura, agora Celsius", C)

#9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é: ́K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
C = float(input("Digite uma temperatura em Celsius: "))
K = round(C + 273.15, 2)
print("A temperatura, agora em Kelvin", K)

#10. Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s (metros por segundo). A formula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.
K = float(input("Digte uma velocidade em km/h (quilômetros por hora): "))
M = round(K/3.6, 2)
print("A conversão dessa velocida para m/s (metros por segundo)", M)

#11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilometros por hora). A fómula de conversão é: K = M ∗ 3.6, sendo K a velocidade em km/h e M em m/s.
M = float(input("Digite uma velocidade em m/s (metros por segundo): "))
K = round(M * 3.6, 2)
print("A conversão dessa velocidade para km/h (quilômetros por hora)", K)
 
#12. Leia uma distancia em milhas e apresente-a convertida em quilômetros A fórmula de conversao  é:̃ K = 1, 61 ∗ M, sendo K a distancia em quilômetros é M em milhas.
M = float(output("Digite uma distância em milha: ", 50))