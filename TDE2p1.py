# TDE2.ALGORITMOS
#1. Faça um programa que leia um número inteiro e o imprima.
numero_inteiro = int(input("Digite um número inteiro: "))
print(numero_inteiro)

#2. Faça um programa que leia um número real e o imprima.
numero_real = float(input("Digite um número real: "))
print(numero_real)

#3. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
valor1 = int(input("Digite um número: "))
valor2 = int(input("Digite outro número: "))
valor3 = int(input("Digite mais outro número: "))
soma = valor1 + valor2 + valor3
print(f"A soma dos três valores é {soma}")

#4. Leia um número real e imprima o resultado do quadrado desse número.
numero_real = float(input("Digite um número real: "))
quadrado_numero = numero_real**2
print(f"Aqui o quadrado desse número {quadrado_numero}")

#5. Leia um número real e imprima a quinta parte deste número.
numero_real = float(input("Digite um número: "))
quinta_parte = round(numero_real/5, 2)
print(f"A quinta parte desse número é {quinta_parte}")

#6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. A formula de conversão é: F = C∗(9.0/5.0) + 32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
C = float(input("Digite uma temperatura em Celsius, para converter ela em Fahrenheit: "))
F = round(C * (9.0/5.0) + 32.0, 2)
print(f"A temperatura, agora em Fahrenheit, é {F}°F")

#7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A formula de conversão é: C = 5.0 ∗ (F − 32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
F = float(input("Digite uma temperatura em Fahrenheit, para converter ela em Celsius: "))
C = round(5.0 * (F - 32.0)/9.0, 2)
print(f"A temperatura, agora em Celsiusé {C}°C")

#8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A formula de conversão é: ́C = K − 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
K = float(input("Digite uma temperatura em Kelvin, para converter ela em Celsius: "))
C = round(K - 273.15, 2)
print (f"A temperatura, agora Celsius é {C}°C")

#9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A fórmula de conversão é: ́K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
C = float(input("Digite uma temperatura em Celsius, para converter ela em Kelvin: "))
K = round(C + 273.15, 2)
print(f"A temperatura, agora em Kelvin {K} K")

#10. Leia uma velocidade em km/h (quilometros por hora) e apresente-a convertida em m/s (metros por segundo). A formula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.
K = float(input("Digite uma velocidade em km/h (quilômetros por hora), para converter ela em m/s (metros por segundo): "))
M = round(K/3.6, 2)
print(f"A conversão dessa velocida para m/s (metros por segundo) é {M}m/s")

#11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilometros por hora). A fómula de conversão é: K = M ∗ 3.6, sendo K a velocidade em km/h e M em m/s.
M = float(input("Digite uma velocidade em m/s (metros por segundo), para converter ela em km/h (quilometros por hora): "))
K = round(M * 3.6, 2)
print(f"A conversão dessa velocidade para km/h (quilômetros por hora) é {K}km/h")
 
#12. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversao  é:̃ K = 1.61 ∗ M, sendo K a distancia em quilômetros é M em milhas.
M = float(input("Digite uma distância em milhas, para converter ela em km/h (quilometros por hora): "))
K = round(1.61 * M, 2)
print(f"A conversão dessa distância, em quilômetros, é {K}km/h")

#13. Leia uma distância em quilômetros e apresente-a convertida em milhas. A fórmula de  ́conversão é:  ́ M = K/1,61 , sendo K a distância em quilômetros e M em milhas.
K = float(input("Digite uma distância em quilômetros, para converter ela em milhas: "))
M = round(K/1.61, 2)
print(f"A conversão dessa distância, em milhas, é {M}mi")

#14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R = G ∗ π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.
G = float(input("Digite um ângulo em graus, para converter ele em radiano: "))
π = 3.14
R = round(G * π/180, 2)
print(f"A conversão desse ângulo, em radianos, é {R}rad")

#15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversãoo ̃: G = R ∗ 180/π, sendo G o angulo em graus e R em radianos e π = 3.14.
R = float(input("Digite um ângulo em radiano, para converter ele em graus: "))
π = 3.14
G = round(R * 180/π, 2)
print(f"A conversão desse ângulo, em graus, é {G}°")

#16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. A fórmula de conversão ̃é: ́C = P ∗ 2, 54, sendo C o comprimento em centımetros e P o comprimento em polegadas.
P = float(input("Digite um valor de comprimento em polegadas, para converter ele em centímetros: "))
C = round(P * 2.54, 2)
print(f"A conversão desse comprimento, em centrómetros, é {C}cm")

#17.Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. A fórmula de conversão ̃é: P = C/2,54, sendo C o comprimento em centÍmetros e P o comprimento em polegadas.
C = float(input("Digite um valor de comprimento em centímetros, para converter ele em polegadas: "))
P = round(C/2.54, 2)
print(f"A conversão desse comprimento, em polegadas, é {P}in")

#18. Leia um valor de volume em metros cubicos m3 e apresente-o convertido em litros. A fórmula de conversão ̃é: ́L = 1000 ∗ M, sendo L o volume em litros e M o volume em metros cúbicos.
M = float(input("Digite um valor de volume em metros cúbicos, para converter ele em litros: "))
L = round(1000 * M, 2)
print(f"A conversão desse volume, em litros, é {L}L")

#19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3. A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.
L = float(input("Digite um valor de volume em litros, para converter ele em metros cúbicos m3: "))
M = round(L/1000, 2)
print(f"A conversão desse volume, em metros cúbicos, é {M}m³")

#20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
K = float(input("Digite um valor de massa em quilogramas, para converter ele em libras: "))
L = round(K/0.45, 2)
print(f"A conversão desse valor, em libras, é {L}lb")

#21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K * 0.45, sendo K a massa em quilogrmas e L a massa em libras.
L = float(input("Digite um valor de massa em libras, para converter ele em quilogramas: "))
K = round(L * 0.45, 2)
print(f"A conversão desse valor, em quilogramas é {K}kg")

#22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
J = float(input("Digite um valor de comprimento em jardas, para converter ele em metros: "))
M = round(0.91 * J, 2)
print(f"A conversão desse valor de comprimento, em metros, é {M}m")

#23. Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de convesão é: J = M/0.91, sendo J o comprimento em jardas e M o comprimento em metros.
M = float(input("Digite um valor de comprimento em metros, para converter ele em jardas: "))
J = round(M/0.91, 2)
print(f"A conversão desse valor de comprimento, em jardas é {J}yd")

#24. Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres. A fórmula de conversão é: A = M * 0.000247, sendo M a áres em metros quadrados e A a área em acres.
M = float(input("Digite um valor de área em metros quarados, para converter ele em acres: "))
A = round(M * 0.000247, 2)
print(f"A conversão desse valor de área, em acres, é {A} acres")

#25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m2. A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a áres em acres.
A = float(input("Digite um valor de área em acres, para converter ele em metros quadrados: "))
M = round(A * 4048.58, 2)
print(f"A conversão desse valor área valor, em metros quadrados, é {M}m²")

#26. Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares. A fórmula de conversão é: H = M * 0.0001, sendo M a áres em metros quadrados e H a área em hectares.
M = float(input("Digite um valor de área em metros quadrados, para converter ele em hectares: "))
H = round(M * 0.0001, 2)
print(f"A conversão desse valor de área, em hectares, é {H}ha")

#27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2. A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
H = float(input("Digite um valor de áres em hectares, para converter ele em metros quadrados: "))
M = round(H * 10000, 2)
print(f"A conversão desse valor de área, em metros quarados, é {M}m²")

#28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
valor1 = float(input("Digite um valor: "))
valor2 = float(input("Digite outro valor: "))
valor3 = float(input("Digite mais um valor: "))

soma = valor1**2 + valor2**2 + valor3**2 
print (f"A soma dos quadrados dos três valores é {soma}")

#29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media_aritmetica = (n1 + n2 + n3 + n4)/4 
print (f"A media aritmética das três notas é {media_aritmetica}")

#30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
real = float(input("Digite um valor na moeda Real: "))
cotacao = float(input("Digite o valor da cotação atual do dólar: "))
conversao = (real/cotacao)
print (f"Valor do real correspondente em dólar é US${conversao:.2f}")

#31. Leia um número inteiro e imprima seu antecessor e seu sucessor.
numero = int(input("Digite um número inteiro para imprimir seu antecessor e seu sucessor: "))
antecessor = numero - 1
sucessor = numero + 1
print(f"O antecessor desse número é {antecessor} e o sucessor desse número é {sucessor}")

#32. Leia um número  inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
numero = int(input("Digite um número inteiro para imprimir a soma do sucessor de seu triplo, com o antecessor de seu dobro: "))
soma = (numero * 3 + 1) + (numero * 2 - 1)
print(f"O resultado dessa soma é {soma}")

#33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
lado_de_um_quadrado = float(input("Digite o tamanho do lado de um quadrado, para imprimor a área: "))
area = round(lado_de_um_quadrado**2, 2)
print(f"O resultado da área é {area}")

#34. Leia o valor do raio de um círculo e calcule  e imprima a área do círculo correspondente. A área do círculo é π * raio2, considere π = 3.141592.
R = float(input("Digite o valor de um raio de um círculo para imprimir a área do círculo correspondente: "))
π = 3.141592
area = round(π * R**2, 2)
print(f"O resultado da área do círculo é {area}")

#35. Sejam a e b catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = raizquadrada a2 + b2. Faça um programa que receba os valores de a e b calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
import math

a = float(input("Digite o valor do cateto 'a' de um triângulo para imprimir o calculo do valor da hipotenusa: "))
b = float(input("Digite o valor do cateto 'b' de um triângulo para imprimir o calculo do valor da hipotenusa: "))

hipotenusa = math.sqrt(a**2 + b**2)
print(f"O resultado do calculo da hipotenusa é {hipotenusa}")

#36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio2 * altura, onde π = 3.141592.
altura = float(input("Digite a altura de um cilindro circular para imprimir o volume do cilindro: "))
raio = float(input("Digite o raio de um cilindro circular para imprimir o volume do cilindro: "))

π = 3.141592
volume = π * raio**2 * altura
print(f"O volume do cilindro circular é {volume}")

#37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.
valor_produto = float(input("Digite o valor de um produto para imprimir um novo valor, mas com desconto de 12%: "))

desconto = valor_produto * 0.12
novo_valor = valor_produto - desconto
print(f"O novo valor do produto é R${novo_valor:.2f}")

#38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
salario = float(input("Digite o salário para obter um novo valor com aumento de 25%: "))

aumento = salario * 0.25
novo_salario = salario + aumento
print(f"O novo salário é R${novo_salario:.2f}")

#39. A importância de R$780.000,00, será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
# O primeiro ganhador receberá 46%; O segundo receberá 32%; O terceiro receberá o restante;
#Calcule e imprima a quantia ganha por cada um dos ganhadores.
importancia1 = 780000.00

primeiro = importancia1 * 0.46
segundo = importancia1 * 0.32
importancia3 = importancia1 - primeiro - segundo

terceiro = importancia3

print(f"O primeiro ganhador receberá R${primeiro:.2f}")
print(f"O segundo ganhador receberá R${segundo:.2f}")
print(f"O terceiro ganhador receberá R${terceiro:.2f}")

#40. Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
dias = float(input("Digite o número de dias trabalhados pelo encanador que cobra 30 reais pela diaria: "))
pagamento = 30 * dias
desconto = pagamento * 0.08
pagamento_liquido = pagamento - desconto 
print(f"A quantidade líquida que deverá ser paga ao encanador, com desconto de 8%, é R${pagamento_liquido:.2f}")

#41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
valor_do_trabalho = float (input("Digite o valor da hora de trabalho, em reais: "))
horas_de_trabalho = float (input("Digite o número de horas trabalhadas no mês: "))

pagamento = valor_do_trabalho * horas_de_trabalho
pagamento_adicional = pagamento * 0.10
pagamento_final = pagamento + pagamento_adicional

print(f"O valor a ser pago ao funcionário, com o adicional de 10%, é R${pagamento_final:.2f}")

#42. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
salario = float(input("Digite o salário-base: "))
gratificacao = salario * 0.05
desconto = salario * 0.07

pagamento_gratificacao = gratificacao + salario
pagamento_final = pagamento_gratificacao - desconto
print(f"Salário final a ser recebido, já com a gratificação e o desconto do imposto, é R${pagamento_final:.2f}")

#43. Escreva um programa de ajude para vendedores. A partir de um valor total lido, mostre:
#o total a pagar com desconto de 10%; o valor de cada parcela, no parcelamento de 3x sem juros; a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto); a comisão do vendedor, no caso de venda ser parcelada (5% sobre o valor total).
valor = float(input("Digite um valor total: "))
valor_total = valor - (valor * 0.10)

parcelas = valor/3
comissao_avista = valor_total * 0.05
comissao_parcela = valor * 0.05

print(f"O valor total é de R${valor:.2f}. Com desconto de 10%, é de R${valor_total:.2f}.")
print(f"No caso de parcelar o valor em três vezes, as parcelas ficam R${parcelas:.2f}. A comissão do vendedor fica R${comissao_parcela:.2f}.")
print(f"No caso de pagar à vista, a comissão do vendedor é R${comissao_avista:.2f}.")

#44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
degrau = float(input("Digite a altura do degrau de uma escada: "))
altura = float(input("Dgite a altura que deseja alcançar subindo a escada: "))
degraus = round(altura/degrau, 2)

print(f"Para atingir o objetivo, {degraus} degraus devem ser subidos")

#45. Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.
letra_maiuscula = input("Digite uma letra maiúscula para converter ela em minúscula: ")
letra_minuscula = chr(ord(letra_maiuscula) + 32)

print(letra_minuscula)

#46. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 900). Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
#NúmeroLido = 123; NúmeroGERADO = 321.
numero_lido = int(input("Digite um número inteiro positivo de três dígitos (de 100 a 999), para gerar outro número formado pelos dígitos invertidos: "))
numero_string = str(numero_lido)
numero_gerado = numero_string [::-1]
resultado = int(numero_gerado)

print(resultado)

#47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
numero_inteiro = int(input("Digite um número inteiro de 4 dígitos (1000 a 9999) para imprimir seus dígitos linha por linha: "))
numero_string = str(numero_inteiro)
for um_por_um in numero_string:
    print (um_por_um)

#48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
segundos = int(input("Digite um valor inteiro em segundos, para imprimir em horas, minutos e segundos: "))
horas = segundos // 3600
restinho1 = segundos % 3600

minutos = restinho1 //60
restinho2_segundos = restinho1 % 60

print(f"{horas}Hr, {minutos}min, {restinho2_segundos}s")

#49. Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) de termino da mesma. 
print("Digite a hora, minuto e segundos do INÍCIO de uma experiêcnia biológica.")
horas_iniciais = int(input("Hora inicial: "))
minutos_iniciais = int(input ("Minuto inicial: "))
segundos_iniciais = int(input ("Segundo inicial: "))

print("Digite quantos segundos de DURAÇÃO da experiêcnia biológica.")
segundos_duracao = int(input ("Segundos duração: "))


segundos1 = segundos_iniciais + segundos_duracao
segundos2 = segundos1 % 60
_c_min = segundos1 // 60

minutos1 = minutos_iniciais + _c_min
minutos2 = _c_min % 60
_c_hr = _c_min // 60

hora1 = (horas_iniciais + _c_hr) % 24

print(f"{hora1}Hr:{minutos2}min:{segundos2}s")

#50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
print("Para saber seu ano de nascimento, digite sua idade e o ano atual.")
idade = int(input("Idade: "))
ano_atual = int(input("Ano atual: "))

ano_nasci = ano_atual - idade
print(f"O ano de nascimento corresponde a {ano_nasci}")

#51. Escreva um programa que leia as coordenadas x e y de pontos no R^2 e calcule sua distância da origem (0, 0).
import math

print("Digite as coordenadas x e de y no R^2, para calcular a distância da origem (0, 0).")
x = float(input("x = "))
y = float(input("y = "))

distancia = math.sqrt(x**2 + y**2)
print (distancia)

#52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu, o valor o prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
print("Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada um deu para a realização da aposta.")
amigo1 = float(input("Digite quanto o amigo 1 deu: "))
amigo2 = float(input("Digite quanto o amigo 2 deu: "))
amigo3 = float(input("Digite quanto o amigo 3 deu: "))

premio = float(input("Digite o valor do prêmio: "))

juncao = amigo1 + amigo2 + amigo3

valor_amg1 = (amigo1/ juncao) * premio
valor_amg2 = (amigo2/juncao) * premio
valor_amg3 = (amigo3/juncao) * premio

print(f"O prêmio do amigo 1 é de R${valor_amg1:.2f}. O prêmio do amigo 2 é de R${valor_amg2:.2f}. O prêmio do amigo 3 é de R${valor_amg3:.2f}")

#53. Faça um programa para ler as dimensões de um terro (comprimento c e largura l), bem como o preço de metro de tela p. Imprima o custo para cercar este mesmo terreno com tela.
print("Digite as dimensões de um terreno e o preço do metro da tela para calcular o custo de como seria cercar.")
c = float(input("Digite o comprimento: "))
l = float(input("Digite a largura: "))
p = float(input("Digite o preço do metro da tela: "))

perimetro = (c * l)
valor = perimetro * p
print(valor)