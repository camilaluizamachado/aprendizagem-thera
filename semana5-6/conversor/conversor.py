dollar = 5.34   # 1 dólar = 5.34 reais
euro = 6.69     # se quiser atualizar, coloque o correto
operacao = ""

while operacao != "5":
    operacao = input("Escolha uma operação: \n1 - Converter de real para dólar\n2 - Converter de real para euro\n3 - Converter de dólar para real\n4 - Converter de euro para real\n5 - Sair\n")

    if operacao == "1":
        valor = float(input("Digite o valor em real: "))
        resultado = valor / dollar
        print(f"{valor} reais = {resultado:.2f} dólares.")

    elif operacao == "2":
        valor = float(input("Digite o valor em real: "))
        resultado = valor / euro
        print(f"{valor} reais = {resultado:.2f} euros.")

    elif operacao == "3":
        valor = float(input("Digite o valor em dólares: "))
        resultado = valor * dollar
        print(f"{valor} dólares = {resultado:.2f} reais.")

    elif operacao == "4":
        valor = float(input("Digite o valor em euros: "))
        resultado = valor * euro
        print(f"{valor} euros = {resultado:.2f} reais.")

    elif operacao == "5":
        print("Saindo...")
        break

    else:
        print("Operação inválida.")
