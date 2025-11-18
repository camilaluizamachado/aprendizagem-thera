import requests

def pegar_cotacao(par):
    url = f"https://economia.awesomeapi.com.br/json/last/{par}"
    resposta = requests.get(url).json()
    chave = par.replace("-", "")
    return float(resposta[chave]["bid"])

while True:
    print("\n1 - Real → Dólar")
    print("2 - Real → Euro")
    print("3 - Dólar → Real")
    print("4 - Euro → Real")
    print("5 - Sair")

    op = input("Opção: ")

    if op == "5":
        print("Saindo...")
        break

    valor = float(input("Valor: ").replace(",", "."))

    if op == "1":
        cot = pegar_cotacao("USD-BRL")
        print(f"{valor} reais = {valor / cot:.2f} dólares (cotação {cot})")

    elif op == "2":
        cot = pegar_cotacao("EUR-BRL")
        print(f"{valor} reais = {valor / cot:.2f} euros (cotação {cot})")

    elif op == "3":
        cot = pegar_cotacao("USD-BRL")
        print(f"{valor} dólares = {valor * cot:.2f} reais (cotação {cot})")

    elif op == "4":
        cot = pegar_cotacao("EUR-BRL")
        print(f"{valor} euros = {valor * cot:.2f} reais (cotação {cot})")

    else:
        print("Opção inválida.")
