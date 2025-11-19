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
