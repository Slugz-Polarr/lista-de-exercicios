nome = input("Digite o nome: ")
temp = float(input("Digite a temperatura: "))

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
velocidade = float(input("Digite a velocidade: "))

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

nome6 = input("Digite o nome: ")
volume = int(input("Digite o volume: "))

print(f"Olá {nome6}, o volume está em {volume} e é considerado: {audio}.")

if volume == 0:
    audio = "Mudo"

elif volume >= 1 and volume <= 20:
    audio = "Muito baixo"

elif volume >= 21 and volume <= 40:
    audio = "Baixo"

elif volume >= 41 and volume <= 60:
    audio = "Médio"

elif volume >= 61 and volume <= 80:
    audio = "Alto"

elif volume >= 81 and volume <= 100:
    audio = "Perigoso"

else:
    audio = "Valor inválido"

print("--------------------------------------------------------------------------------------------------------------")

nome7 = input("Digite o nome: ")
hora = int(input("Digite a hora: "))

print(f"Olá {nome7}, agora são {hora}h e estamos no período: {periodo}.")

if hora >= 0 and hora <= 5:
    periodo = "Madrugada"

elif hora >= 6 and hora <= 11:
    periodo = "Manhã"

elif hora >= 12 and hora <= 17:
    periodo = "Tarde"

elif hora >= 18 and hora <= 21:
    periodo = "Noite"

elif hora >= 22 and hora <= 23:
    periodo = "Noite tardia"

else:
    periodo = "Hora inválida"

print("--------------------------------------------------------------------------------------------------------------")

nome8 = input("Digite o nome: ")
fome = int(input("Digite o nível de fome: "))

print(f"Olá {nome8}, seu nível de fome é {fome} e está: {nivel}.")

if fome == 0:
    nivel = "Sem fome"

elif fome >= 1 and fome <= 3:
    nivel = "Pouca"

elif fome >= 4 and fome <= 6:
    nivel = "Média"

elif fome >= 7 and fome <= 8:
    nivel = "Alta"

elif fome >= 9 and fome <= 10:
    nivel = "Extrema"

else:
    nivel = "Valor inválido"

print("--------------------------------------------------------------------------------------------------------------")

nome9 = input("Digite o nome: ")
altura = float(input("Digite a altura em metros: "))

print(f"Olá {nome9}, você mede {altura}m e é considerado: {classe}.")

if altura < 1.60:
    classe = "Baixo"

elif altura >= 1.60 and altura <= 1.75:
    classe = "Médio"

elif altura >= 1.76 and altura <= 1.90:
    classe = "Alto"

else:
    classe = "Gigante"

print("--------------------------------------------------------------------------------------------------------------")

nome10 = input("Digite o nome: ")
stress = int(input("Digite o nível de stress: "))

print(f"Olá {nome10}, seu nível de stress é {stress} e está: {quantia}.")

if stress >= 0 and stress <= 2:
    quantia = "Tranquilo"

elif stress >= 3 and stress <= 5:
    quantia = "Leve"

elif stress >= 6 and stress <= 7:
    quantia = "Médio"

elif stress >= 8 and stress <= 9:
    quantia = "Alto"

elif stress == 10:
    quantia = "Extremo"

else:
    quantia = "Valor inválido"

print("--------------------------------------------------------------------------------------------------------------")