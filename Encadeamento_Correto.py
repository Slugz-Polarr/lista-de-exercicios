nome = input("Digite o nome: ")
temp = float(input("Digite a temperatura (°C): "))

print(f"Olá {nome}, a temperatura é {temp}°C e está: {clima}.")

if temp < 0:
    clima = "Congelante"

elif temp >= 0 and temp <= 10:
    clima = "Muito frio"

elif temp >= 11 and temp <= 20:
    clima = "Frio"

elif temp >= 21 and temp <= 25:
    clima = "Agradável"

elif temp >= 26 and temp <= 30:
    clima = "Quente"

elif temp >= 31 and temp <= 35:
    clima = "Muito quente"

else:
    clima = "Inferno"

print("--------------------------------------------------------------------------------------------------------------")

nome2 = input("Digite o nome: ")
pontos = int(input("Digite os pontos: "))

print(f"Olá {nome2}, você tem {pontos} pontos e seu rank é: {rank}.")

if pontos < 500:
    rank = "Ferro"

elif pontos >= 500 and pontos <= 999:
    rank = "Bronze"

elif pontos >= 1000 and pontos <= 1999:
    rank = "Prata"

elif pontos >= 2000 and pontos <= 2999:
    rank = "Ouro"

elif pontos >= 3000 and pontos <= 3999:
    rank = "Platina"

else:
    rank = "Diamante"

print("--------------------------------------------------------------------------------------------------------------")

nome3 = input("Digite o nome: ")
salario = float(input("Digite o salário: "))

print(f"Olá {nome3}, seu salário é R${salario} e seu limite é: R${limite}.")

if salario < 1000:
    limite = 0

elif salario >= 1000 and salario <= 2000:
    limite = 500

elif salario >= 2001 and salario <= 4000:
    limite = 1000

elif salario >= 4001 and salario <= 7000:
    limite = 3000

else:
    limite = 5000

print("--------------------------------------------------------------------------------------------------------------")

nome4 = input("Digite o nome: ")
nota = float(input("Digite a nota: "))

print(f"Olá {nome4}, sua nota foi {nota} e seu desempenho é: {resultado}.")

if nota < 3:
    resultado = "Péssimo"

elif nota >= 3 and nota <= 4.9:
    resultado = "Ruim"

elif nota >= 5 and nota <= 6.9:
    resultado = "Regular"

elif nota >= 7 and nota <= 8.4:
    resultado = "Bom"

elif nota >= 8.5 and nota <= 9.4:
    resultado = "Muito bom"

else:
    resultado = "Excelente"

print("--------------------------------------------------------------------------------------------------------------")

nome5 = input("Digite o nome: ")
velocidade = float(input("Digite a velocidade (km/h): "))

print(f"Olá {nome5}, você estava a {velocidade} km/h e sua infração é: {infracao}.")

if velocidade <= 60:
    infracao = "OK"

elif velocidade >= 61 and velocidade <= 80:
    infracao = "Leve"

elif velocidade >= 81 and velocidade <= 100:
    infracao = "Média"

elif velocidade >= 101 and velocidade <= 120:
    infracao = "Grave"

else:
    infracao = "Gravíssima"

print("--------------------------------------------------------------------------------------------------------------")