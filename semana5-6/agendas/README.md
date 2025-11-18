# Agenda de Contatos em Python

Este projeto contém duas versões de um sistema de **agenda de contatos** em Python:  

1. **Versão em memória (temporária)**  
2. **Versão persistente usando JSON**

---

## 1. Versão em memória

- Todos os contatos ficam armazenados apenas na memória durante a execução.  
- Ao fechar o programa, todos os contatos são perdidos.  
- Permite:
  - Adicionar contatos
  - Listar contatos
  - Buscar contatos  

**Como usar:**

```bash
python agenda_memoria.py
Exemplo de uso:

yaml
Copiar código
Quantos contatos deseja salvar? 2
Contato 1:
Nome: Camila
Telefone: 11999999999
Contato 2:
Nome: Rafael
Telefone: 11988888888

=== Lista de Contatos ===
Camila               11999999999
Rafael               11988888888

Digite o nome que deseja buscar: Camila
Nome: Camila, Telefone: 11999999999
⚠️ Limitação: ao fechar o programa, os contatos não são salvos.

2. Versão persistente (JSON)
Os contatos são armazenados em um arquivo agenda.json, permitindo que os dados persistam entre execuções.

Permite:

Adicionar contatos

Listar contatos

Buscar contatos

Excluir contatos

Como usar:

bash
Copiar código
python agenda_json.py
Exemplo de uso:

makefile
Copiar código
=== Agenda ===
1 - Adicionar contato
2 - Listar contatos
3 - Buscar contato
4 - Excluir contato
5 - Sair
Escolha: 1
Nome: Camila
Telefone: 11999999999
Contato adicionado.

Escolha: 2
=== Contatos ===
Nome: Camila             Telefone: 11999999999
✅ Todos os contatos ficam salvos no arquivo agenda.json.

