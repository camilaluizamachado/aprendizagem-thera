import json
import os

# Caminho do arquivo JSON da agenda
CAMINHO_AGENDA = os.path.join(os.path.dirname(__file__), "agenda.json")

def carregar_agenda():
    """Carrega a lista de contatos da agenda."""
    if not os.path.exists(CAMINHO_AGENDA):
        return []  # Retorna lista vazia se não existir
    with open(CAMINHO_AGENDA, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_agenda(agenda):
    """Salva a lista de contatos da agenda no arquivo JSON."""
    with open(CAMINHO_AGENDA, "w", encoding="utf-8") as f:
        json.dump(agenda, f, ensure_ascii=False, indent=4)
