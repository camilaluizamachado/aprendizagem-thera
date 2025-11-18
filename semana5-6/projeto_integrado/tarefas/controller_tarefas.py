from .storage_tarefas import carregar, salvar

def menu_tarefas():
    while True:
        print("\n=== Tarefas ===")
        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Remover")
        print("4 - Voltar")

        op = input("Opção: ")

        if op == "1":
            adicionar()
        elif op == "2":
            listar()
        elif op == "3":
            remover()
        elif op == "4":
            break
        else:
            print("Opção inválida.")

def adicionar():
    lista = carregar()
    nome = input("Nome da tarefa: ")
    lista.append({"nome": nome})
    salvar(lista)
    print("Tarefa adicionada.")

def listar():
    lista = carregar()
    if not lista:
        print("Nenhuma tarefa.")
        return

    print("\nTarefas:")
    for i, t in enumerate(lista, start=1):
        print(f"{i}. {t['nome']}")

def remover():
    lista = carregar()
    listar()

    try:
        idx = int(input("Número da tarefa a remover: "))
        lista.pop(idx - 1)
        salvar(lista)
        print("Tarefa removida.")
    except:
        print("Número inválido.")
