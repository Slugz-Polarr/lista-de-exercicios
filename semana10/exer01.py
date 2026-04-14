idade = int(input("Digite sua idade: "))
autorizacao = input("Possui autorização: ")

if idade >= 18 or autorizacao == "sim":
    print("Catraca Liberada! ")
else:
    print("Catraca Bloqueada!") 