import tkinter as tk
from tkinter import messagebox

# Funções da calculadora
def adicionar(valor):
    visor.insert(tk.END, valor)

def limpar():
    visor.delete(0, tk.END)

def apagar():
    texto = visor.get()[:-1]
    visor.delete(0, tk.END)
    visor.insert(0, texto)

def calcular():
    try:
        expressao = visor.get()
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except Exception:
        messagebox.showerror("Erro", "Expressão inválida")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.config(bg="#1e1e1e")

# Campo de exibição
visor = tk.Entry(janela, font=("Arial", 20), justify="right", bg="#2c2c2c", fg="white", border=0)
visor.pack(padx=10, pady=20, fill="x")

# Layout de botões
botoes = [
    ["C", "←", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "" , ""]
]

frame_botoes = tk.Frame(janela, bg="#1e1e1e")
frame_botoes.pack()

for linha in botoes:
    linha_frame = tk.Frame(frame_botoes, bg="#1e1e1e")
    linha_frame.pack(expand=True, fill="both")
    for botao in linha:
        if botao == "":
            tk.Label(linha_frame, text="", bg="#1e1e1e").pack(side="left", expand=True, fill="both")
            continue

        cor = "#2c2c2c" if botao not in ["C", "←", "="] else "#ff5252" if botao == "C" else "#00b894" if botao == "=" else "#ffb142"
        btn = tk.Button(
            linha_frame,
            text=botao,
            bg=cor,
            fg="white",
            font=("Arial", 16),
            border=0,
            activebackground="#555",
            command=(
                lambda x=botao: limpar() if x == "C"
                else apagar() if x == "←"
                else calcular() if x == "="
                else adicionar(x)
            )
        )
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

janela.mainloop()
