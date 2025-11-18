def criar_agenda():
    contatos = []

    num = int(input("Quantos contatos deseja salvar? "))

    for i in range(num):
        print(f"\nContato {i+1}:")
        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()

        # validação básica
        if not nome or not telefone.isdigit():
            print("⚠️ Nome ou número inválido, pulando...")
            continue

        contatos.append({"nome": nome, "telefone": telefone})

    return contatos


def mostrar_agenda(contatos):
    if not contatos:
        print("\nAgenda vazia.")
        return

    print("\n=== Lista de Contatos ===")
    for c in contatos:
        print(f"{c['nome']:<20} {c['telefone']}")
    print()


def buscar_contato(contatos):
    termo = input("\nDigite o nome que deseja buscar: ").strip().lower()

    resultados = [c for c in contatos if termo in c['nome'].lower()]

    if resultados:
        print("\nResultado(s) encontrado(s):")
        for c in resultados:
            print(f"Nome: {c['nome']}, Telefone: {c['telefone']}")
    else:
        print("Nenhum contato encontrado.")


def main():
    contatos = criar_agenda()
    mostrar_agenda(contatos)
    buscar_contato(contatos)


if __name__ == "__main__":
    main()