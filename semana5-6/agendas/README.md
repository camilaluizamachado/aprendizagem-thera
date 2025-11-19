# Agenda de Contatos em Python

Sistema de gerenciamento de contatos em Python com duas versões:

1. **Versão em memória (temporária)** – os dados são perdidos ao fechar o programa.  
2. **Versão persistente usando JSON** – os dados são salvos em `agenda.json` e permanecem entre execuções.

---

## Funcionalidades

### Versão em memória
- Adicionar contatos  
- Listar contatos  
- Buscar contatos  
- ⚠️ Limitação: os dados não são salvos após encerrar o programa

### Versão persistente (JSON)
- Adicionar contatos  
- Listar contatos  
- Buscar contatos  
- Excluir contatos  
- ✅ Todos os contatos são salvos automaticamente em `agenda.json`

---

## Pré-requisitos
- Python 3.x instalado

## Exemplos de uso
### Versão em memória
 - Quantos contatos deseja salvar? 2
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

### Versão persistente (JSON)
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

## Estrutura do projeto
agenda_memoria.py    # Versão em memória
agenda_json.py       # Versão persistente com JSON
agenda.json          # Arquivo de armazenamento dos contatos
README.md            # Este arquivo

