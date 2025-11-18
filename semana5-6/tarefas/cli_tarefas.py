import json
import os
from datetime import datetime

ARQUIVO = "tarefas_cli.json"


def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)


def listar(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa.")
        return
    print("\n--- TAREFAS ---")
    for i, t in enumerate(tarefas):
        status = "✔️" if t["feito"] else "❌"
        print(f"{i+1}. {t['titulo']} [{status}] — prazo: {t['prazo']}")


def adicionar(tarefas):
    titulo = input("Título: ")
    prazo = input("Prazo (AAAA-MM-DD): ")
    try:
        datetime.strptime(prazo, "%Y-%m-%d")
    except:
        print("Prazo inválido.")
        return
    tarefas.append({"titulo": titulo, "prazo": prazo, "feito": False})
    salvar(tarefas)


def concluir(tarefas):
    listar(tarefas)
    idx = int(input("Número: ")) - 1
    tarefas[idx]["feito"] = True
    salvar(tarefas)


def remover(tarefas):
    listar(tarefas)
    idx = int(input("Número: ")) - 1
    tarefas.pop(idx)
    salvar(tarefas)


def menu():
    tarefas = carregar()

    while True:
        print("\n1 Listar\n2 Adicionar\n3 Concluir\n4 Remover\n5 Sair")
        op = input("Opção: ")

        if op == "1":
            listar(tarefas)
        elif op == "2":
            adicionar(tarefas)
        elif op == "3":
            concluir(tarefas)
        elif op == "4":
            remover(tarefas)
        elif op == "5":
            break
        else:
            print("Inválido.")


menu()
