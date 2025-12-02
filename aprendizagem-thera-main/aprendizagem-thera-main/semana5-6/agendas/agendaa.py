import json
import os

ARQUIVO = "agenda.json"

def carregar_agenda():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_agenda(agenda):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)

def adicionar_contato(agenda):
    nome = input("Nome: ").strip()
    telefone = input("Telefone: ").strip()
    contato = {"nome": nome, "telefone": telefone}
    agenda.append(contato)
    salvar_agenda(agenda)
    print("Contato adicionado.")

def listar_contatos(agenda):
    if not agenda:
        print("Agenda vazia.")
        return
    for contato in agenda:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")

def buscar_contato(agenda):
    nome = input("Buscar nome: ").strip()
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}")
            return
    print("Contato não encontrado.")

def excluir_contato(agenda):
    nome = input("Nome do contato para excluir: ").strip()
    for contato in agenda:
        if contato["nome"].lower() == nome.lower():
            agenda.remove(contato)
            salvar_agenda(agenda)
            print("Contato removido.")
            return
    print("Contato não encontrado.")

def menu():
    agenda = carregar_agenda()
    while True:
        print("\nAgenda:")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Excluir contato")
        print("5 - Sair")

        opc = input("Escolha: ")

        if opc == "1":
            adicionar_contato(agenda)
        elif opc == "2":
            listar_contatos(agenda)
        elif opc == "3":
            buscar_contato(agenda)
        elif opc == "4":
            excluir_contato(agenda)
        elif opc == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
