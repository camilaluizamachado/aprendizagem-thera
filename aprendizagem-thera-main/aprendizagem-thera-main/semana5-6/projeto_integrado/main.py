from agenda.controller_agenda import menu_agenda
from tarefas.controller_tarefas import menu_tarefas

def main():
    while True:
        print("\n=== SISTEMA INTEGRADO ===")
        print("1 - Agenda")
        print("2 - Tarefas")
        print("3 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            menu_agenda()
        elif opcao == "2":
            menu_tarefas()
        elif opcao == "3":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
