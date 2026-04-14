nome = input("Digite o nome do jogador: ")
pontuacao = int(input("Digite a pontuação: "))

if pontuacao < 1000:
    nivel = "Iniciante"

elif pontuacao >= 1000 and pontuacao <= 3000:
    nivel = "Casual"

elif pontuacao >= 3001 and pontuacao < 7000:
    nivel = "Pro"

else: 
    nivel = "Lenda"

print(f"Olá {nome}, você fez {pontuacao} pontos e seu nível é: {nivel}.")

print("--------------------------------------------------------------------------------------------------------------")

nome2 = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

print(f"Olá {nome2}, você tem {idade} anos e seu estilo recomendado é: {estilo}.")

if idade < 12:
    estilo = "Infantil"

elif idade >= 13 and idade <= 17:
    estilo = "Pop/Funk"

elif idade >= 18 and idade <= 25:
    estilo = "Rock/Metal"

else:
    estilo = "Variado"

print("--------------------------------------------------------------------------------------------------------------")

nome3 = input("Digite seu nome: ")
valor = int(input("Digite o valor do pedido: "))

print(f"Olá {nome3}, seu pedido foi de R${valor} e é classificado como: {pedido}.")

if valor < 20:
    pedido = "Simples"

elif valor >= 20 and valor <= 50:
    pedido = "Médio"

elif valor >= 51 and valor <= 100:
    pedido = "Grande"

else:
    pedido = "VIP"

print("--------------------------------------------------------------------------------------------------------------")

nome4 = input("Digite seu nome: ")
peso = int(input("Digite o valor do pedido: "))

print(f"Olá {nome4}, você levantou {peso}kg e seu nível é: {supino}.")

if peso < 40:
    supino = "iniciante"

elif peso >= 40 and peso <= 80:
    supino = "intermediário"

elif peso >= 81 and peso < 120:
    supino = "Avançado"

else:
    supino = "Monstro"

print("--------------------------------------------------------------------------------------------------------------")

nome5 = input("Digite o nome do aluno: ")
media = float(input("Digite a média do aluno: "))

print(f"Olá {nome5}, sua média foi {media} e seu desempenho é: {desempenho}.")

if media < 5:
    desempenho = "Reprovado"

elif media >= 5 and media <= 6.9:
    desempenho = "Recuperação"

elif media >= 7 and media <= 8.9:
    desempenho = "Bom"

else:
    desempenho = "Excelente"

print("--------------------------------------------------------------------------------------------------------------")

nome6 = input("Digite o nome: ")
horas = float(input("Quantas horas por dia usa o celular? "))

print(f"Olá {nome6}, você usa o celular {horas} horas por dia e seu uso é: {uso}.")

if horas < 2:
    uso = "Baixo"

elif horas >= 2 and horas <= 5:
    uso = "Moderado"

elif horas >= 6 and horas <= 8:
    uso = "Alto"

else:
    uso = "Excessivo"

print("--------------------------------------------------------------------------------------------------------------")

nome7 = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

print(f"Olá {nome7}, você tem {idade} anos e pode assistir filmes: {classificacao}.")

if idade < 10:
    classificacao = "Infantil"

elif idade >= 10 and idade <= 13:
    classificacao = "Livre"

elif idade >= 14 and idade <= 17:
    classificacao = "+14"

else:
    classificacao = "Adulto"

print("--------------------------------------------------------------------------------------------------------------")

nome8 = input("Digite o nome: ")
saldo = float(input("Digite o saldo bancário: "))

print(f"Olá {nome8}, seu saldo é R${saldo} e sua situação é: {situacao}.")

if saldo < 0:
    situacao = "Endividado"

elif saldo >= 0 and saldo <= 100:
    situacao = "Baixo"

elif saldo >= 101 and saldo <= 1000:
    situacao = "Estável"

else:
    situacao = "Confortável"

print("--------------------------------------------------------------------------------------------------------------")

nome9 = input("Digite o nome: ")
velocidade = float(input("Digite a velocidade do carro: "))

print(f"Olá {nome9}, você está a {velocidade} km/h e isso é: {situacao2}.")

if velocidade < 40:
    situacao2 = "Lento"

elif velocidade >= 40 and velocidade <= 80:
    situacao2 = "Normal"

elif velocidade >= 81 and velocidade <= 120:
    situacao2 = "Rápido"

else:
    situacao2 = "Perigoso"

print("--------------------------------------------------------------------------------------------------------------")

nome10 = input("Digite o nome: ")
horas = float(input("Quantas horas joga por dia? "))

print(f"Olá {nome10}, você joga {horas} horas por dia e é classificado como: {classe}.")

if horas < 1:
    classe = "Casual"

elif horas >= 1 and horas <= 3:
    classe = "Jogador"

elif horas >= 4 and horas <= 6:
    classe = "Gamer"

else:
    classe = "Hardcore"

print("--------------------------------------------------------------------------------------------------------------")
