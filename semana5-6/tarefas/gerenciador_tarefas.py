import json
import os

CAMINHO_ARQUIVO = r"C:\Users\Windows\aprendizagem-thera\aprendizagem-thera-main\semana5-6\tarefas\tarefas.json"

def carregar_tarefas():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return []
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_tarefas(tarefas):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

tarefas = carregar_tarefas()

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    op = input("Opção: ")

    if op == "1":
        nova = input("Digite a nova tarefa: ")
        tarefas.append(nova)
        salvar_tarefas(tarefas)
        print("Tarefa adicionada.")

    elif op == "2":
        if not tarefas:
            print("Nenhuma tarefa.")
        else:
            print("\nTarefas:")
            for i, t in enumerate(tarefas):
                print(f"{i+1}. {t}")

    elif op == "3":
        if not tarefas:
            print("Nenhuma tarefa para remover.")
        else:
            indice = int(input("Número da tarefa para remover: ")) - 1
            if 0 <= indice < len(tarefas):
                removida = tarefas.pop(indice)
                salvar_tarefas(tarefas)
                print(f"Tarefa removida: {removida}")
            else:
                print("Número inválido.")

    elif op == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
