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

