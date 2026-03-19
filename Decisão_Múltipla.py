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
    supino - "Monstro"

print("--------------------------------------------------------------------------------------------------------------")

