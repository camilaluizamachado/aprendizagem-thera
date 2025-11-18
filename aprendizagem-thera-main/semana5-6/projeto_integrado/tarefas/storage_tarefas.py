import json
import os

CAMINHO = os.path.join(os.path.dirname(__file__), "tarefas.json")

def carregar():
    if not os.path.exists(CAMINHO):
        return []  # lista vazia se não existir

    with open(CAMINHO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(lista):
    with open(CAMINHO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
