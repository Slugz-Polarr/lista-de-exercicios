nota = float(input("Digite sua nota: "))

if nota >= 7:
    print("Aprovado.")
elif nota >= 5 and nota <= 6.9:
    print("Recuperação.")
else:
    print("Reprovado.")

print("-------------------------------------------------------")

horas = float(input("Digite seu tempo jogado: "))

if horas <= 2:
    print("Tempo saudável.")
elif horas >= 3 and horas <= 4.9:
    print("Jogou bastante hoje.")
else:
    print("Hora de descansar e estudar.")

print("-------------------------------------------------------")

seguidores = float(input("digite sua quantidade de seguidores: "))

if seguidores <= 499:
    print("Perfil pequeno.")
elif seguidores >= 500 and seguidores <= 4999:
    print("Perfil em crescimento.")
else:
    print("Influencer da escola.")

print("-------------------------------------------------------")

bateria = float(input("Digite sua porcentagem de bateria: "))

if bateria >= 60:
    print("Bateria alta.")
elif bateria <= 30 and bateria >= 59:
    print("Bateria média.")
else:
    print("Corre carregar o celular.")

print("-------------------------------------------------------")

tempo = float(input("Digite seu tempo: "))

if tempo <= 30:
    print("Uso moderado.")
elif tempo >= 31 and tempo <= 119:
    print("Você passou um bom tempo.")
else:
    print("Você vive no TikTiok.")

print("-------------------------------------------------------")

pontuacao = float(input("Digite sua pontuação: "))

if pontuacao <= 1000:
    print("Iniciante.")
elif 