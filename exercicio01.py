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

if seguidores <= 500:
    print("Perfil pequeno.")
elif seguidores >= 501 and seguidores <= 4999:
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
elif tempo >= 31 and tempo <= 120:
    print("Você passou um bom tempo.")
else:
    print("Você vive no TikTiok.")

print("-------------------------------------------------------")

pontuacao = float(input("Digite sua pontuação: "))

if pontuacao <= 1000:
    print("Iniciante.")
elif pontuacao >= 1001 and pontuacao <= 4999:
    print("Jogador intermediário.")
else:
    print("Jogador profissional.")

print("-------------------------------------------------------")

qunt_faltas = float(input("Digite suas faltas: "))


if qunt_faltas <= 5:
    print("Frequência excelente.")
elif qunt_faltas >= 6 and qunt_faltas <= 14:
    print("Fique atento às faltas.")
else:
    print("Risco de reprovação.")

print("-------------------------------------------------------")

idade = float(input("Digite sua idade: "))

if idade <= 13:
    print("Muito jovem para redes sociais.")
elif idade >= 14 and idade <= 17:
    print("Adolescente.")
else:
    print("Adulto.")

print("-------------------------------------------------------")

estudo = float(input("Digite quantas horas você estudou hoje: "))

if estudo <= 0:
    print("Precisa estudar.")
elif estudo >= 1 and estudo <= 2:
    print("Bom esforço.")
else:
    print("Aluno dedicado.")

print("-------------------------------------------------------")

espaço = float(input("Digite a quantidade de espaço livre: "))

if espaço <= 5:
    print("Celular quase cheio.")
elif espaço >= 5 and espaço <= 20:
    print("Espaço razoável.")
else:
    print("Muito espaço livre.")

print("-------------------------------------------------------")

streaming = float(input("Digite horas assistidas: "))

if streaming <= 1:
    print("Assistiu pouco.")
elif streaming >= 2 and streaming <= 3:
    print("Maratonando.")
else:
    print("Maratona pesada.")