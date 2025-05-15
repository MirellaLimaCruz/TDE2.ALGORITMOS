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
print("A conversão dessa velocidade para km/h (quilômetros por hora) é: ", K)
 
#12. Leia uma distância em milhas e apresente-a convertida em quilômetros A fórmula de conversao  é:̃ K = 1.61 ∗ M, sendo K a distancia em quilômetros é M em milhas.
M = float(input("Digite uma distância em milha: ", 50))
K = round(1.61 * M, 2)
print("A conversão dessa distância, em quilômetros, é: ")

#13. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de  ́conversão é:  ́ M = K/1,61 , sendo K a distância em quilômetros e M em milhas.
K = float(input("Digite uma distância em quilômetros: "))
M = round(K/1.61, 2)
print("A conversão dessa distância, em milhas, é: ")

#14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G ∗ π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.
G = float(input("Digite um ângulo em graus: "))
π = 3.14
R = round(G * π/180, 2)
print("A conversão desse ângulo, em radianos, é: ", R)

#15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversãoo ̃: G = R ∗ 180/π, sendo G o angulo em graus e R em radianos e π = 3.14.
R = float(input("Digite um ângulo em radiano: "))
π = 3.14
G = round(R * 180/π, 2)
print("A conversão desse ângulo, em graus, é: ", G)

#16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão ̃é: ́C = P ∗ 2, 54, sendo C o comprimento em centımetros e P o comprimento em polegadas.
P = float(input("Digite um valor de comprimento em polegadas: "))
C = round(P * 2.54, 2)
print("A conversão desse comprimento, em centrómetros, é: ", C)

#17.Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A fórmula de conversão ̃é: P = C/2,54, sendo C o comprimento em centÍmetros e P o comprimento em polegadas.
C = float(input("Digite um valor de comprimento em centímetros: "))
P = round(C/2.54, 2)
print("A conversão desse comprimento, em polegadas, é: ", P)

#18. Leia um valor de volume em metros cubicos m3 e apresente-o convertido em litros. A fórmula de conversão ̃é: ́L = 1000 ∗ M, sendo L o volume em litros e M o volume em metros cúbicos.
M = float(input("Digite um valor de volume em metros cúbicos: "))
L = round(1000 * M, 2)
print("A conversão desse volume, em litros, é: ", L)


#19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3. A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.
L = float(input("Digite um valor de volume em litros: "))
M = round(L/1000, 2)
print("A conversão desse volume, em metros cúbicos, é: ", M)

#20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
K = float(input("Digite um valor de massa em quilogramas: "))
L = round(K/0.45, 2)
print("A conversão desse valor, em libras, é: ", L)

#21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K * 0.45, sendo K a massa em quilogrmas e L a massa em libras.
L = float(input("Digite um valor de massa em libras: "))
K = round(L * 0.45, 2)
print("A conversão desse valor, em quilogramas é: ", K)

#22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
J = float(input("Digite um valor de comprimento em jardas: "))
M = round(0.91 * J, 2)
print("A conversão desse valor de comprimento, em metros, é",M)

#23. Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de convesão é: J = M/0.91, sendo J o comprimento em jardas e M o comprimento em metros.
M = float(input("Digite um valor de comprimento em metros: "))
J = round(M/0.91, 2)
print("A conversão desse valor de comprimento, em jardas é: ", J)

#24. Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres. A fórmula de conversão é: A = M * 0.000247, sendo M a áres em metros quadrados e A a área em acres.
M = float(input("Digite um valor de área em metros quarados: "))
A = round(M * 0.000247, 2)
print("A conversão desse valor de área, em acres, é: ", A)

#25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m2. A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a áres em acres.
A = float(input("Digite um valor de área em acres: "))
M = round(A * 4048.58, 2)
print("A conversão desse valor área valor, em metros quadrados, é: ", M)

#26. Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares. A fórmula de conversão é: H = M * 0.0001, sendo M a áres em metros quadrados e H a área em hectares.
M = float(input("Digite um valor de área em metros quadrados: "))
H = round(M * 0.0001, 2)
print("A conversão desse valor de área, em hectares, é: ", H)

#27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2. A fórmula de conversão é: M = H * 10000, sendo M a áres em metros quadrados e H a área em hectares.
H = float(input("Digite um valor de áres em hectares: "))
M = round(H * 10000, 2)
print("A conversão desse valor de área, em metros quarados, é: ", M)

#28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
Valor1 = float(input("Digite um valor: "))
Valor2 = float(input("Digite outro valor: "))
Valor3 = float(input("Digite mais um valor: "))

soma = Valor1**2 + Valor2**2 + Valor3**2 
print ("A soma dos quadrados dos três valores é: ", soma)

#29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media_aritmetica = (n1 + n2 + n3 + n4)/4 
print ("A media aritmética das três notas é: ", media_aritmetica)

#30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
real = float(input("Digite um valor na moeda Real: "))
cotacao = float(input("Digite o valor da cotação atual do dólar: "))
conversao = round(real/cotacao, 2)
print ("Valor do real, correspondente em dólar é: ", conversao)

#31. Leia um número inteiro e imprima seu antecessor e seu sucessor.
numero = int(input("Digite um número inteiro para imprimir seu antecessor e seu sucessor: "))
antecessor = numero - 1
sucessor = numero + 1
print ("O antecessor desse número é: ", antecessor, ". E o sucessor desse número é: ", sucessor)

#32. Leia um número  inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
numero = int(input("Digite um número inteiro para imprimir a soma do sucessor de seu triplo, com o antecessor de seu dobro: "))
soma = round((numero * 3 + 1) + (numero * 2 - 1), 2)
print("O resultado dessa soma é: ", soma)

#33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
lado_de_um_quadrado = float(input("Digite o tamanho do lado de um quadrado, para imprimor a área: "))
area = lado_de_um_quadrado**2
print("O resultado da área é:", area)

#34. Leia o valor do raio de um círculo e calcule  e imprima a área do círculo correspondente. A área do círculo é π * raio2, considere π = 3.141592.
R = float(input("Digite o valor de um raio de um círculo para imprimir a área do círculo correspondente: "))
π = 3.141592
area = round(π * R**2, 2)
print("O resultado da área do círculo é: ", area)
