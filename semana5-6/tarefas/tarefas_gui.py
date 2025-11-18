import PySimpleGUI as sg
import json
import os

ARQUIVO = "tarefas_gui.json"

def carregar():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)

tarefas = carregar()

layout = [
    [sg.Text("Tarefas")],
    [sg.Listbox(values=[t["titulo"] for t in tarefas], size=(40, 10), key="LISTA")],
    [sg.Input(key="NOVA"), sg.Button("Adicionar")],
    [sg.Button("Concluir"), sg.Button("Remover"), sg.Button("Sair")]
]

janela = sg.Window("Gerenciador de Tarefas", layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Sair":
        break

    if evento == "Adicionar":
        titulo = valores["NOVA"].strip()
        if titulo:
            tarefas.append({"titulo": titulo, "feito": False})
            salvar(tarefas)
            janela["LISTA"].update([t["titulo"] for t in tarefas])

    if evento == "Remover":
        selecionado = valores["LISTA"]
        if selecionado:
            titulo = selecionado[0]
            tarefas = [t for t in tarefas if t["titulo"] != titulo]
            salvar(tarefas)
            janela["LISTA"].update([t["titulo"] for t in tarefas])

    if evento == "Concluir":
        selecionado = valores["LISTA"]
        if selecionado:
            titulo = selecionado[0]
            for t in tarefas:
                if t["titulo"] == titulo:
                    t["feito"] = True
            salvar(tarefas)

janela.close()
