import json
import os

CAMINHO_AGENDA = "agenda/agenda.json"

def carregar_agenda():
    if not os.path.exists(CAMINHO_AGENDA):
        return []
    with open(CAMINHO_AGENDA, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_agenda(agenda):
    with open(CAMINHO_AGENDA, "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)

def adicionar_contato():
    nome = input("Nome: ")
    telefone = input("Telefone: ")

    agenda = carregar_agenda()
    agenda.append({"nome": nome, "telefone": telefone})
    salvar_agenda(agenda)

    print("Contato adicionado com sucesso!")

def listar_contatos():
    agenda = carregar_agenda()
    if not agenda:
        print("Nenhum contato salvo.")
        return

    print("\n--- CONTATOS ---")
    for c in agenda:
        print(f"{c['nome']} - {c['telefone']}")

def menu_agenda():
    while True:
        print("\n=== AGENDA ===")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Voltar")

        opcao = input("Opção: ")

        if opcao == "1":
            adicionar_contato()
        elif opcao == "2":
            listar_contatos()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")
